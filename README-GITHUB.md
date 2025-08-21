# Continuum

> **Never explain your project twice to AI coding assistants**

Continuum is a lightweight, project-scoped memory system that preserves context between AI-assisted coding sessions without consuming tokens or requiring manual updates.

## 🎯 The Problem

Every AI coding session looks like this:
```
You: "Read PROJECT.md, TODO.md, CHANGELOG.md to understand what we're working on..."
AI: *burns 2000+ tokens reading files*
You: "Also check recent commits..."  
AI: *burns more tokens*
You: "Now we can finally start working on..."
```

**Result:** Wasted tokens, slow session starts, manual progress tracking, redundant documentation files.

## ✨ The Solution

```bash
cd your-project
continuum                    # One-time setup
# Just start coding - everything tracked automatically
```

```bash
# Next session - AI gets instant context
curl http://localhost:8000/context
# "Phase: Authentication | Last: Fixed JWT validation | Next: Add 2FA"
```

**That's it.** Zero manual updates, zero token waste, instant context recovery.

## 🚀 Quick Start

### Installation
```bash
curl -sSL https://raw.githubusercontent.com/yourusername/continuum/main/install.sh | bash
```

### Usage
```bash
cd your-project
continuum                    # Auto-setup (once per project)
# Start coding normally - everything tracks automatically
```

### AI Integration
Add to your Claude Code/Gemini CLI session:
```
Project context available at: curl http://localhost:8000/context
Use this instead of reading project files.
```

## 🧠 How It Works

**Intelligent Auto-Tracking:**
- 📁 **File changes** → "Modified authentication system"
- 🔄 **Git commits** → "Implemented user login"  
- 📦 **Package installs** → "Added React Router v6"
- 🧪 **Test runs** → "All tests passing (15/15)"
- 🌿 **Branch switches** → "Working on feature/auth"

**Smart Pattern Recognition:**
```bash
# AI detects: 5 .sol files modified + test files
# Auto-logs: "Smart contract development session"

# AI detects: package.json change + migration files  
# Auto-logs: "Database schema update"
```

## 🎁 Features

### ✅ Core Features
- **Zero-token context loading** - API provides instant project status
- **Automatic activity tracking** - File changes, commits, commands, tests
- **Project-scoped memory** - Each project gets independent context
- **Git integration** - Commits automatically logged with smart categorization
- **Cross-platform** - Works on Linux, macOS, Windows
- **Language agnostic** - Supports any project type

### 🤖 AI Assistant Integration
- **Claude Code** - Instant context via API calls
- **Gemini CLI** - Built-in integration commands
- **Cursor** - VS Code extension support
- **Any AI tool** - Standard REST API

### 📊 Smart Analytics
- **Session detection** - Knows when you start/stop coding
- **Pattern recognition** - "Testing phase" vs "Bug fixing" vs "Feature development"
- **Progress tracking** - Automatic milestone detection
- **Time-based archiving** - Keeps memory files clean

## 📖 Examples

### Web Development
```bash
cd my-react-app
continuum
# Auto-detects: React project, sets up web template
# Tracks: Component changes, npm installs, build runs
```

### Blockchain Development  
```bash
cd my-defi-project
continuum
# Auto-detects: Solidity files, sets up blockchain template
# Tracks: Contract deployments, test runs, migrations
```

### Data Science
```bash
cd ml-experiment
continuum  
# Auto-detects: Jupyter notebooks, Python files
# Tracks: Model training, data processing, experiments
```

## 🛠️ Advanced Usage

### Session Management
```bash
continuum start              # Start tracked session
continuum status             # Check current project state
continuum summary            # Get human-readable summary
continuum archive            # Clean old entries
```

### API Endpoints
```bash
GET  /context               # Optimized for AI consumption
GET  /summary               # Human-readable status
POST /log                   # Manual logging
POST /phase                 # Set project phase
GET  /history               # Full session history
```

### Templates
```bash
continuum init --template web        # React/Vue/Angular setup
continuum init --template backend    # API development setup  
continuum init --template blockchain # Solidity/Web3 setup
continuum init --template data       # ML/Data science setup
```

## 🔧 Configuration

### Auto-tracking Rules
```json
{
  "patterns": {
    "*.sol + test/": "Smart contract development",
    "package.json + migrations/": "Database schema update",
    "*.tsx + *.test.*": "Frontend feature development"
  }
}
```

### Git Hook Customization
```bash
continuum hooks install              # Install git hooks
continuum hooks configure            # Customize hook behavior
```

## 🏗️ Architecture

```
Project Directory/
├── .claude-memory.json              # Active memory (lightweight)
├── .claude-memory-archive.json      # Historical data
└── .git/hooks/post-commit          # Auto-commit logging

Continuum Installation/
├── bin/continuum                    # Main CLI
├── bin/mem                          # Memory management
├── server.py                        # Local API server
└── templates/                       # Project templates
```

## 🤝 Contributing

We welcome contributions! Areas where help is needed:

- **IDE Integrations** - VS Code, JetBrains, Vim extensions
- **AI Tool Integrations** - More AI coding assistants
- **Pattern Recognition** - Smarter activity detection
- **Project Templates** - More language/framework templates
- **Performance** - Optimization for large projects

See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

## 📄 License

MIT License - see [LICENSE](LICENSE) for details.

## 🌟 Why This Matters

**The AI coding revolution is here**, but context management is broken. Developers waste time and tokens explaining their projects to AI assistants every session.

Continuum fixes this with:
- 🚀 **Instant context recovery** - No more "read these files first"
- 💰 **Token savings** - Eliminate redundant file reads
- 🤖 **Universal compatibility** - Works with any AI coding tool
- 📈 **Better outcomes** - AI understands your project deeply from session one

## 📞 Support

- 💬 **Discord** - [discord.com/channels/1367156542305996820/1407795520415600782](https://discord.com/channels/1367156542305996820/1407795520415600782)
- 🐛 **Issues** - [GitHub Issues](https://github.com/rezurx/Continuum/issues)
- 🐦 **Twitter** - [@CeviphantRezurx](https://x.com/CeviphantRezurx)

---

**⭐ Star this repo if Continuum saves you time and tokens!**