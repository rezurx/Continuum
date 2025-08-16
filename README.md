# Continuum - Persistent Memory for AI Coding Sessions

**Continuum** is a lightweight, project-scoped memory system designed to preserve context between AI-assisted coding sessions (e.g. Claude Code, Gemini CLI, etc.) **without consuming model context or tokens**.

## ✨ What it does

- 📝 Log what you worked on, problems solved, and what's next
- 🔄 Resume future sessions by loading a small summary instead of re-explaining everything  
- 🔍 Maintain searchable history of decisions, fixes, and milestones
- 📦 Automatically record commit activity
- 🌐 Expose everything via local API so any agent can access/update memory autonomously

**In short**: Makes AI agents persistent and aligned across sessions — turning isolated prompts into a continuous development thread.

## 🚀 Quick Start

**TL;DR**: `cd your-project && continuum` - that's it! 🎉

### 1. Install Dependencies
```bash
# Ubuntu/Debian
sudo apt install jq

# macOS
brew install jq

# Python dependencies for API server
pip install fastapi uvicorn
```

### 2. Add to PATH
```bash
# Add to ~/.bashrc or ~/.zshrc
export PATH="$HOME/dev/continuum/bin:$PATH"

# Reload shell
source ~/.bashrc
```

### 3. Auto-Setup Any Project
```bash
cd your-project
continuum  # Automatically sets up memory, git hooks, and imports existing docs
```

**What auto-setup does:**
- Creates `.claude-memory.json` if it doesn't exist
- Installs git commit hook (if git repo)
- **Detects existing documentation** (README.md, TODO.md, PROGRESS.md, etc.)
- **Offers smart import** of existing project context
- **Auto-archives original files** to `.continuum-imported/` after import
- Shows current project status

### 4. Manual Initialization (Alternative)
```bash
cd your-project
mem init --template web  # or backend, data, or basic
```

### 5. Start Using
```bash
mem phase "Setting up authentication"
mem log "Added JWT middleware" --type decision
mem next "Implement user registration"
mem show --summary
```

## 📖 CLI Commands

### Core Commands
```bash
mem phase "Description"              # Set current project phase
mem log "What happened" [--type]     # Log activity (note|error|decision|commit)
mem next "Task description"          # Add to next tasks
mem done "Task description"          # Mark task as completed
```

### Viewing & Analysis
```bash
mem show                            # Show full memory file
mem show --summary                  # Show last 3 entries + next tasks
mem show --last 5                   # Show last 5 entries
mem show --errors                   # Show only error entries
mem show --decisions                # Show only decision entries
mem show --commits                  # Show only commit entries
mem context                         # Optimized output for AI agents
```

### Management
```bash
mem archive                         # Archive entries older than 30 days
mem archive --days 14               # Archive entries older than 14 days
mem init --template web             # Initialize with template (web|backend|data)
```

## 📦 Smart Import & Auto-Archive

### Automatic Documentation Detection
When you run `continuum` in a project with existing documentation, it automatically detects and offers to import:
- `PROJECT.md`, `README.md`, `TODO.md`, `PROGRESS.md`
- `CHANGELOG.md`, `NOTES.md`, `progress.md`, `todo.md`

### Smart Content Parsing
The import process automatically extracts:
- **Current phase/status** from headers like "Current", "Status", "Phase", "Working on"
- **Completed items** from lines containing "completed", "done", "finished"
- **Todo/next items** from lines containing "todo", "next", "pending", "task"
- **Decisions** from lines containing "decision", "chose", "using", "decided"

### Safe Auto-Archive
After successful import:
- Original files are moved to `.continuum-imported/` directory
- Files can be restored with: `mv .continuum-imported/* .`
- Archive can be deleted when confident: `rm -rf .continuum-imported/`
- **Your original files are never lost!**

### Manual Import
```bash\ncontinuum import  # Shows step-by-step import instructions\n```

## 🔗 Git Integration

### Auto-commit Logging
```bash
# Copy hook to a git project
cp ~/dev/continuum/hooks/post-commit .git/hooks/
chmod +x .git/hooks/post-commit
```

### Install Across All Projects
```bash
find ~/dev -name ".git" -type d -exec sh -c 'cp ~/dev/continuum/hooks/post-commit {}/hooks/post-commit && chmod +x {}/hooks/post-commit' \;
```

## 🌐 API Server

### Start Server
```bash
cd your-project
python ~/dev/continuum/server.py
```

Server runs at `http://127.0.0.1:8000` with interactive docs at `/docs`

### API Endpoints
```bash
# Get summary for AI agents
curl http://127.0.0.1:8000/summary

# Get optimized context
curl http://127.0.0.1:8000/context

# Add log entry
curl -X POST http://127.0.0.1:8000/log \
  -H "Content-Type: application/json" \
  -d '{"notes":"Fixed login bug","type":"note"}'

# Set project phase
curl -X POST http://127.0.0.1:8000/phase \
  -H "Content-Type: application/json" \
  -d '{"phase":"Testing phase"}'

# Add next task
curl -X POST http://127.0.0.1:8000/next \
  -H "Content-Type: application/json" \
  -d '{"task":"Add error handling"}'

# Mark task completed
curl -X POST http://127.0.0.1:8000/done \
  -H "Content-Type: application/json" \
  -d '{"task":"Add error handling"}'
```

## 🤖 AI Agent Integration

### For Claude Code
Add this to your session or CLAUDE.md:
```
You can access project context via: curl http://127.0.0.1:8000/context
To log progress: curl -X POST http://127.0.0.1:8000/log -H "Content-Type: application/json" -d '{"notes":"description","type":"note"}'
Use the API instead of tracking progress in conversation.
```

### Manual Context Loading
```bash
# Paste this output to any AI agent
mem context
```

## 📁 File Structure

```
~/dev/continuum/
├── bin/mem                     # Main CLI script
├── server.py                   # API server
├── hooks/post-commit           # Git hook template
├── templates/
│   └── claude-memory-template.json
└── README.md
```

### Project Files (auto-created)
```
your-project/
├── .claude-memory.json         # Main memory file
└── .claude-memory-archive.json # Archived entries
```

## 💡 Example Workflows

### New Project Setup
```bash
cd my-new-project
continuum                    # Auto-setup: memory + hooks + status

# Start tracking progress
mem phase "API refactoring"
mem log "Switched from REST to GraphQL" --type decision
mem next "Update client SDK"
```

### Existing Project with Documentation
```bash
cd existing-project          # Has README.md, TODO.md, etc.
continuum                    # Detects docs, offers import
# Choose: 1) Yes - import automatically
#         2) No  - skip and continue

# After import, original files safely moved to .continuum-imported/
mem show --summary           # See imported context
```

### Daily Development
```bash
# Log decisions and progress
mem log "Database migration completed" --type note
mem next "Write integration tests"

# View current state
mem show --summary

# Complete tasks
mem done "Update client SDK"

# Let AI agent access context
curl http://127.0.0.1:8000/context
```

## 🛠️ Templates

### Web Template
- Phase: "Frontend Setup"
- Tasks: Set up build tools, Create component structure, Add routing

### Backend Template  
- Phase: "API Development"
- Tasks: Design schema, Set up endpoints, Add authentication

### Data Template
- Phase: "Data Pipeline" 
- Tasks: Set up data sources, Create ETL pipeline, Add monitoring

## 🎯 Benefits

✅ **Zero token consumption** - Memory stored locally, not in model context  
✅ **Project-scoped** - Each project has its own memory  
✅ **Agent-agnostic** - Works with Claude, Gemini, or any AI tool  
✅ **Persistent** - Context survives across sessions  
✅ **Searchable** - Filter by type, date, or content  
✅ **Automatic** - Git hooks capture commits automatically  
✅ **Lightweight** - Simple JSON files, no database required