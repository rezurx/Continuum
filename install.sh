#!/bin/bash
# Continuum - One-line installer
# curl -sSL https://raw.githubusercontent.com/rezurx/Continuum/main/install.sh | bash

set -e

CONTINUUM_DIR="$HOME/.continuum"
BIN_DIR="$HOME/.local/bin"

echo "🚀 Installing Continuum..."

# Create directories
mkdir -p "$CONTINUUM_DIR"/{bin,templates,hooks}
mkdir -p "$BIN_DIR"

# Download files
echo "📦 Downloading Continuum files..."
curl -sSL https://raw.githubusercontent.com/rezurx/Continuum/main/bin/continuum > "$CONTINUUM_DIR/bin/continuum"
curl -sSL https://raw.githubusercontent.com/rezurx/Continuum/main/bin/mem > "$CONTINUUM_DIR/bin/mem"
curl -sSL https://raw.githubusercontent.com/rezurx/Continuum/main/server.py > "$CONTINUUM_DIR/server.py"
curl -sSL https://raw.githubusercontent.com/rezurx/Continuum/main/hooks/post-commit > "$CONTINUUM_DIR/hooks/post-commit"
curl -sSL https://raw.githubusercontent.com/rezurx/Continuum/main/templates/claude-memory-template.json > "$CONTINUUM_DIR/templates/claude-memory-template.json"

# Make scripts executable
chmod +x "$CONTINUUM_DIR/bin/continuum"
chmod +x "$CONTINUUM_DIR/bin/mem"
chmod +x "$CONTINUUM_DIR/server.py"
chmod +x "$CONTINUUM_DIR/hooks/post-commit"

# Create symlinks
ln -sf "$CONTINUUM_DIR/bin/continuum" "$BIN_DIR/continuum"
ln -sf "$CONTINUUM_DIR/bin/mem" "$BIN_DIR/mem"

# Check dependencies
echo "🔍 Checking dependencies..."

# Check for jq
if ! command -v jq >/dev/null 2>&1; then
    echo "⚠️  jq not found. Installing..."
    if command -v apt >/dev/null 2>&1; then
        sudo apt update && sudo apt install -y jq
    elif command -v brew >/dev/null 2>&1; then
        brew install jq
    elif command -v yum >/dev/null 2>&1; then
        sudo yum install -y jq
    else
        echo "❌ Could not install jq automatically. Please install it manually:"
        echo "   Ubuntu/Debian: sudo apt install jq"
        echo "   macOS: brew install jq"
        echo "   CentOS/RHEL: sudo yum install jq"
        exit 1
    fi
fi

# Check for Python 3
if ! command -v python3 >/dev/null 2>&1; then
    echo "❌ Python 3 is required but not found. Please install Python 3."
    exit 1
fi

# Install Python dependencies
echo "🐍 Installing Python dependencies..."
if command -v pip3 >/dev/null 2>&1; then
    pip3 install --user fastapi uvicorn
else
    echo "⚠️  pip3 not found. You'll need to install FastAPI and uvicorn manually:"
    echo "   pip3 install fastapi uvicorn"
fi

# Add to PATH if needed
echo "🔧 Configuring PATH..."
SHELL_RC=""
if [ -n "$ZSH_VERSION" ]; then
    SHELL_RC="$HOME/.zshrc"
elif [ -n "$BASH_VERSION" ]; then
    SHELL_RC="$HOME/.bashrc"
else
    SHELL_RC="$HOME/.profile"
fi

if [ -f "$SHELL_RC" ] && ! grep -q "$BIN_DIR" "$SHELL_RC"; then
    echo "export PATH=\"$BIN_DIR:\$PATH\"" >> "$SHELL_RC"
    echo "✅ Added $BIN_DIR to PATH in $SHELL_RC"
    echo "   Run: source $SHELL_RC"
else
    echo "✅ PATH already configured"
fi

echo ""
echo "🎉 Continuum installed successfully!"
echo ""
echo "📚 Quick start:"
echo "   cd your-project"
echo "   continuum"
echo ""
echo "📖 Documentation: https://github.com/rezurx/Continuum"
echo ""
echo "⚠️  If 'continuum' command not found, run: source $SHELL_RC"