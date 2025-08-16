#!/usr/bin/env python3
"""
Continuum Local API Server
Exposes project memory via REST API for AI agents
"""

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import json
import uvicorn
from datetime import datetime
from pathlib import Path
from typing import List, Optional

app = FastAPI(title="Continuum Memory API", version="1.0.0")

MEM_FILE = Path(".claude-memory.json")
ARCHIVE_FILE = Path(".claude-memory-archive.json")

# Models
class LogEntry(BaseModel):
    notes: str
    type: str = "note"

class TaskEntry(BaseModel):
    task: str

class PhaseEntry(BaseModel):
    phase: str

# Utility functions
def load_memory():
    """Load main memory file"""
    if not MEM_FILE.exists():
        return {"current_phase": "", "next_tasks": [], "session_history": [], "decisions": []}
    try:
        with open(MEM_FILE, "r") as f:
            return json.load(f)
    except json.JSONDecodeError:
        return {"current_phase": "", "next_tasks": [], "session_history": [], "decisions": []}

def save_memory(data):
    """Save main memory file"""
    with open(MEM_FILE, "w") as f:
        json.dump(data, f, indent=2)

# API Endpoints
@app.get("/")
def root():
    return {"message": "Continuum Memory API", "version": "1.0.0"}

@app.get("/summary")
def get_summary():
    """Get project memory summary (equivalent to mem show --summary)"""
    mem = load_memory()
    recent = sorted(mem["session_history"], key=lambda x: x["date"], reverse=True)[:3]
    return {
        "current_phase": mem["current_phase"],
        "last_steps": recent,
        "next_tasks": mem.get("next_tasks", [])
    }

@app.get("/context")
def get_context():
    """Get optimized context for AI agents (equivalent to mem context)"""
    mem = load_memory()
    recent = sorted(mem["session_history"], key=lambda x: x["date"], reverse=True)[:2]
    
    context = f"PROJECT CONTEXT:\n"
    context += f"Phase: {mem['current_phase']}\n"
    context += "Last 2 activities:\n"
    for item in recent:
        context += f"- {item['notes']}\n"
    context += "Next tasks:\n"
    for task in mem.get("next_tasks", []):
        context += f"- {task}\n"
    
    return {"context": context}

@app.post("/log")
def add_log(entry: LogEntry):
    """Add log entry (equivalent to mem log)"""
    mem = load_memory()
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
    
    mem["session_history"].append({
        "date": timestamp,
        "notes": entry.notes,
        "type": entry.type
    })
    
    save_memory(mem)
    return {"status": "logged", "entry": entry.notes}

@app.post("/phase")
def set_phase(phase: PhaseEntry):
    """Set current project phase (equivalent to mem phase)"""
    mem = load_memory()
    mem["current_phase"] = phase.phase
    save_memory(mem)
    return {"status": "phase_set", "phase": phase.phase}

@app.post("/next")
def add_task(task: TaskEntry):
    """Add task to next_tasks (equivalent to mem next)"""
    mem = load_memory()
    mem["next_tasks"].append(task.task)
    save_memory(mem)
    return {"status": "task_added", "task": task.task}

@app.post("/done")
def complete_task(task: TaskEntry):
    """Mark task as completed (equivalent to mem done)"""
    mem = load_memory()
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
    
    # Add completion log
    mem["session_history"].append({
        "date": timestamp,
        "notes": f"Completed: {task.task}",
        "type": "completion"
    })
    
    # Remove from next_tasks if it exists
    if task.task in mem["next_tasks"]:
        mem["next_tasks"].remove(task.task)
    
    save_memory(mem)
    return {"status": "task_completed", "task": task.task}

@app.get("/history")
def get_history(type_filter: Optional[str] = None, limit: Optional[int] = 10):
    """Get session history with optional filtering"""
    mem = load_memory()
    history = mem["session_history"]
    
    if type_filter:
        history = [item for item in history if item["type"] == type_filter]
    
    # Sort by date descending and limit
    history = sorted(history, key=lambda x: x["date"], reverse=True)[:limit]
    
    return {"history": history}

@app.get("/tasks")
def get_tasks():
    """Get current next_tasks list"""
    mem = load_memory()
    return {"next_tasks": mem.get("next_tasks", [])}

@app.get("/health")
def health_check():
    """Health check endpoint"""
    return {"status": "healthy", "memory_file_exists": MEM_FILE.exists()}

if __name__ == "__main__":
    print("Starting Continuum Memory API server...")
    print("Access at: http://127.0.0.1:8000")
    print("Docs at: http://127.0.0.1:8000/docs")
    uvicorn.run(app, host="127.0.0.1", port=8000)