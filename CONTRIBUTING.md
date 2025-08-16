# Contributing to Continuum

Thanks for your interest in contributing to Continuum! This guide will help you get started.

## 🎯 Project Vision

Continuum aims to **eliminate the context gap** between AI coding sessions by providing:
- Zero-token context loading for AI assistants
- Automatic activity tracking without manual intervention  
- Universal compatibility across programming languages and AI tools
- Maximum ease of use ("lazy-friendly" design)

## 🚀 Quick Start for Contributors

```bash
git clone https://github.com/yourusername/continuum.git
cd continuum
./install.sh
cd test-project
continuum
```

## 🏗️ Architecture Overview

```
continuum/
├── bin/
│   ├── continuum           # Main CLI (auto-setup)
│   └── mem                 # Memory management CLI
├── server.py               # Local API server
├── enhanced-tracker.py     # Intelligent auto-tracking
├── hooks/
│   └── post-commit        # Git integration
└── templates/
    └── *.json             # Project templates
```

### Core Components

1. **CLI Tools** (`bin/`) - User-facing commands
2. **API Server** (`server.py`) - REST API for AI tools
3. **Auto-Tracker** (`enhanced-tracker.py`) - Smart pattern detection
4. **Git Integration** (`hooks/`) - Automatic commit logging
5. **Templates** (`templates/`) - Project initialization

## 🛠️ Areas for Contribution

### High Impact
- **IDE Integrations** - VS Code, JetBrains, Vim extensions
- **AI Tool Integrations** - More AI coding assistants  
- **Smart Pattern Recognition** - Better activity detection
- **Performance Optimization** - Large project handling

### Medium Impact
- **Project Templates** - More language/framework templates
- **Configuration System** - Customizable tracking rules
- **Cross-platform Support** - Windows compatibility improvements
- **Documentation** - Tutorials, examples, guides

### Low Impact (Good First Issues)
- **Bug fixes** - Small issues and edge cases
- **Error handling** - Better error messages
- **Code cleanup** - Refactoring and optimization
- **Tests** - Unit tests and integration tests

## 📋 Contribution Workflow

### 1. Choose an Issue
- Check [Issues](https://github.com/yourusername/continuum/issues) for bugs/features
- Look for `good-first-issue` labels for beginners
- Comment on issues you want to work on

### 2. Fork and Clone
```bash
git clone https://github.com/YOUR-USERNAME/continuum.git
cd continuum
git checkout -b feature/your-feature-name
```

### 3. Development Setup
```bash
# Install development dependencies
pip install -r dev-requirements.txt

# Run tests
python -m pytest tests/

# Test your changes
cd test-project
../bin/continuum
```

### 4. Make Changes
- Follow existing code style
- Add tests for new features
- Update documentation if needed
- Test with multiple project types

### 5. Submit Pull Request
```bash
git add .
git commit -m "feat: add smart contract template"
git push origin feature/your-feature-name
```

Then create a PR on GitHub.

## 🎨 Code Style Guidelines

### Python Code
```python
# Use type hints
def log_activity(self, description: str, activity_type: str = "auto") -> None:
    
# Use descriptive variable names
def detect_smart_contract_development(self, changed_files: List[str]) -> bool:

# Add docstrings for public methods
def scan_file_changes(self):
    """Scan for file changes and detect patterns"""
```

### Bash Scripts
```bash
# Use set -e for error handling
set -e

# Quote variables
echo "Installing to: $INSTALL_DIR"

# Use descriptive function names
function install_git_hooks() {
```

### JSON/Configuration
```json
{
  "patterns": {
    "description": "Clear description of what this pattern detects",
    "files": ["*.sol", "test/*.js"],
    "activity": "Smart contract testing"
  }
}
```

## 🧪 Testing Guidelines

### Test Types
1. **Unit Tests** - Test individual functions
2. **Integration Tests** - Test component interactions
3. **End-to-End Tests** - Test full workflows
4. **Manual Tests** - Test with real projects

### Test Structure
```python
def test_smart_contract_detection():
    """Test that .sol file changes are detected as contract development"""
    tracker = ContinuumTracker()
    changed_files = ["contracts/Token.sol", "test/Token.test.js"]
    
    activity = tracker.analyze_file_changes(changed_files)
    assert "Smart contract" in activity.description
```

## 📖 Documentation Standards

### README Updates
- Keep examples current and working
- Add new features to feature list
- Update installation instructions if needed

### Code Comments
```python
# Explain WHY, not what
# Good: Check file hash to detect actual content changes (not just timestamp)
file_hash = self._get_file_hash(filepath)

# Bad: Get file hash
file_hash = self._get_file_hash(filepath)
```

### API Documentation
- Document all endpoints
- Include example requests/responses
- Explain error codes

## 🏷️ Issue and PR Labels

### Issue Labels
- `bug` - Something isn't working
- `enhancement` - New feature or improvement  
- `good-first-issue` - Good for newcomers
- `help-wanted` - Extra attention needed
- `documentation` - Documentation updates

### PR Labels  
- `feat` - New feature
- `fix` - Bug fix
- `docs` - Documentation changes
- `refactor` - Code refactoring
- `test` - Adding/updating tests

## 🔧 IDE Integration Development

If you're building IDE extensions:

### VS Code Extension
```typescript
// Use the Continuum API
const response = await fetch('http://localhost:8000/context');
const context = await response.json();

// Show context in status bar
vscode.window.showInformationMessage(`Phase: ${context.phase}`);
```

### Required Features
- **Context Display** - Show current phase/tasks in IDE
- **Auto-logging** - Log file saves, test runs, etc.
- **Quick Actions** - Buttons for common `mem` commands

## 🤖 AI Tool Integration

For new AI tool integrations:

### Required Endpoints
```bash
GET /context     # Optimized context for AI consumption
POST /log        # Log AI session activities  
GET /summary     # Human-readable project status
```

### Integration Examples
```python
# Claude Code integration
context = requests.get('http://localhost:8000/context').json()
print(f"Claude now knows: {context['context']}")

# Log AI activities
requests.post('http://localhost:8000/log', json={
    'notes': 'Generated user authentication system',
    'type': 'ai-generated'
})
```

## 🎁 Reward System

### Recognition
- Contributors get mentioned in releases
- Top contributors get maintainer status
- Special recognition in README

### Swag (Future)
- Continuum stickers for contributors
- T-shirts for major contributions
- Conference talk opportunities

## 📞 Getting Help

- **Discord** - [discord.gg/continuum](https://discord.gg/continuum)
- **GitHub Discussions** - For design questions
- **Email** - maintainers@continuum.dev

## 📄 License

By contributing, you agree that your contributions will be licensed under the MIT License.

---

**Happy coding! 🚀**