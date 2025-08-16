#!/usr/bin/env python3
"""
Continuum Enhanced Auto-Tracker
Intelligent pattern recognition and automatic logging
"""

import os
import json
import time
import subprocess
import re
from datetime import datetime
from pathlib import Path
import hashlib
from typing import Dict, List, Optional

class ContinuumTracker:
    def __init__(self, project_dir: str = "."):
        self.project_dir = Path(project_dir).resolve()
        self.memory_file = self.project_dir / ".claude-memory.json"
        self.state_file = self.project_dir / ".continuum-state.json"
        
        # Load or create state
        self.state = self._load_state()
        
        # Pattern rules for intelligent detection
        self.patterns = {
            # File patterns -> activity descriptions
            "*.sol + test/": "Smart contract development",
            "*.sol + migrations/": "Contract deployment preparation", 
            "package.json + node_modules/": "Dependency management",
            "*.tsx + *.test.*": "Frontend feature development",
            "*.py + requirements.txt": "Python development",
            "Cargo.toml + src/": "Rust development",
            "*.go + go.mod": "Go development",
            "docker* + *.yml": "Infrastructure setup",
            "*.md + docs/": "Documentation updates"
        }
        
        # Command patterns
        self.command_patterns = {
            r"npm (test|run test)": "Running tests",
            r"npm (start|run dev)": "Starting development server", 
            r"npm install": "Installing dependencies",
            r"cargo (build|test)": "Rust build/test",
            r"python.*test": "Running Python tests",
            r"truffle (compile|migrate|test)": "Smart contract operations",
            r"hardhat (compile|test|run)": "Hardhat blockchain operations"
        }
    
    def _load_state(self) -> Dict:
        """Load tracking state"""
        if self.state_file.exists():
            try:
                with open(self.state_file) as f:
                    return json.load(f)
            except:
                pass
        
        return {
            "file_hashes": {},
            "last_scan": 0,
            "session_start": time.time(),
            "commands_run": [],
            "detected_activities": []
        }
    
    def _save_state(self):
        """Save tracking state"""
        with open(self.state_file, 'w') as f:
            json.dump(self.state, f, indent=2)
    
    def _load_memory(self) -> Dict:
        """Load project memory"""
        if self.memory_file.exists():
            try:
                with open(self.memory_file) as f:
                    return json.load(f)
            except:
                pass
        
        return {
            "current_phase": "",
            "next_tasks": [],
            "session_history": [],
            "decisions": []
        }
    
    def _save_memory(self, memory: Dict):
        """Save project memory"""
        with open(self.memory_file, 'w') as f:
            json.dump(memory, f, indent=2)
    
    def _log_activity(self, description: str, activity_type: str = "auto"):
        """Log activity to memory"""
        memory = self._load_memory()
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
        
        # Avoid duplicate recent entries
        recent = [h for h in memory["session_history"] if h.get("date", "").startswith(timestamp[:16])]
        if any(description in h.get("notes", "") for h in recent):
            return
        
        memory["session_history"].append({
            "date": timestamp,
            "notes": description,
            "type": activity_type
        })
        
        self._save_memory(memory)
        print(f"🤖 Auto-logged: {description}")
    
    def _get_file_hash(self, filepath: Path) -> str:
        """Get file content hash"""
        try:
            with open(filepath, 'rb') as f:
                return hashlib.md5(f.read()).hexdigest()
        except:
            return ""
    
    def _scan_file_changes(self):
        """Scan for file changes and detect patterns"""
        changed_files = []
        
        # Scan important file types
        patterns = ["**/*.py", "**/*.js", "**/*.ts", "**/*.tsx", "**/*.sol", 
                   "**/*.go", "**/*.rs", "**/*.java", "**/*.cpp", "**/package.json",
                   "**/requirements.txt", "**/Cargo.toml", "**/go.mod"]
        
        for pattern in patterns:
            for filepath in self.project_dir.glob(pattern):
                if ".git" in str(filepath) or "node_modules" in str(filepath):
                    continue
                
                current_hash = self._get_file_hash(filepath)
                relative_path = str(filepath.relative_to(self.project_dir))
                old_hash = self.state["file_hashes"].get(relative_path)
                
                if old_hash != current_hash:
                    changed_files.append(relative_path)
                    self.state["file_hashes"][relative_path] = current_hash
        
        if changed_files:
            self._analyze_file_changes(changed_files)
    
    def _analyze_file_changes(self, changed_files: List[str]):
        """Analyze file changes and detect activity patterns"""
        
        # Group changes by directory/type
        changes = {
            "contracts": [f for f in changed_files if f.endswith('.sol')],
            "tests": [f for f in changed_files if 'test' in f],
            "frontend": [f for f in changed_files if f.endswith(('.tsx', '.jsx', '.ts', '.js'))],
            "backend": [f for f in changed_files if f.endswith('.py') or f.endswith('.go')],
            "config": [f for f in changed_files if f in ['package.json', 'requirements.txt', 'Cargo.toml']]
        }
        
        # Detect patterns
        if changes["contracts"] and changes["tests"]:
            self._log_activity("Smart contract development with testing", "development")
        elif changes["contracts"]:
            self._log_activity(f"Modified {len(changes['contracts'])} smart contracts", "development") 
        elif changes["frontend"] and changes["tests"]:
            self._log_activity("Frontend feature development with tests", "development")
        elif len(changes["frontend"]) >= 3:
            self._log_activity("Frontend component development", "development")
        elif changes["config"]:
            self._log_activity("Project configuration updates", "config")
        elif changes["tests"]:
            self._log_activity("Test implementation/updates", "testing")
        elif len(changed_files) >= 5:
            self._log_activity(f"Major development session - {len(changed_files)} files modified", "development")
        elif len(changed_files) >= 2:
            # Smart descriptions based on file types
            file_types = set(Path(f).suffix for f in changed_files)
            if '.sol' in file_types:
                self._log_activity("Smart contract modifications", "development")
            elif '.py' in file_types:
                self._log_activity("Python development", "development")
            elif any(ext in file_types for ext in ['.js', '.ts', '.tsx']):
                self._log_activity("JavaScript/TypeScript development", "development")
    
    def _track_commands(self):
        """Track important commands run in this session"""
        try:
            # This is a simplified version - in practice you'd integrate with shell history
            # or use a shell hook to capture commands
            pass
        except:
            pass
    
    def _detect_session_activity(self):
        """Detect high-level session activity"""
        session_duration = time.time() - self.state["session_start"]
        
        # If session > 30 minutes and substantial changes, log as development session
        if session_duration > 1800:  # 30 minutes
            total_files = len(self.state["file_hashes"])
            if total_files > 10:
                self._log_activity("Extended development session", "session")
                self.state["session_start"] = time.time()  # Reset session timer
    
    def scan(self):
        """Run a full scan for changes"""
        print("🔍 Scanning for project changes...")
        
        self._scan_file_changes()
        self._track_commands() 
        self._detect_session_activity()
        
        self.state["last_scan"] = time.time()
        self._save_state()
    
    def start_watching(self, interval: int = 60):
        """Start continuous watching"""
        print(f"👁️  Starting Continuum auto-tracker (scan every {interval}s)")
        print("   Press Ctrl+C to stop")
        
        try:
            while True:
                self.scan()
                time.sleep(interval)
        except KeyboardInterrupt:
            print("\n🛑 Auto-tracker stopped")
    
    def get_session_summary(self) -> str:
        """Get summary of current session activity"""
        memory = self._load_memory()
        recent_activities = [
            h for h in memory["session_history"] 
            if h.get("type") in ["auto", "development", "testing", "config"]
        ][-5:]  # Last 5 auto-logged activities
        
        if not recent_activities:
            return "No automatic activities detected this session"
        
        summary = "Recent automated tracking:\n"
        for activity in recent_activities:
            summary += f"  - {activity['notes']} ({activity['date']})\n"
        
        return summary

def main():
    import sys
    
    if len(sys.argv) > 1:
        command = sys.argv[1]
        tracker = ContinuumTracker()
        
        if command == "scan":
            tracker.scan()
        elif command == "watch":
            interval = int(sys.argv[2]) if len(sys.argv) > 2 else 60
            tracker.start_watching(interval)
        elif command == "summary":
            print(tracker.get_session_summary())
        else:
            print("Usage: enhanced-tracker.py [scan|watch|summary]")
    else:
        print("Continuum Enhanced Auto-Tracker")
        print("Usage: enhanced-tracker.py [scan|watch|summary]")

if __name__ == "__main__":
    main()