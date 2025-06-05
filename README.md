# SmolCC 🤖

<div align="center">

**A Lightweight Code Assistant with Powerful Tool Integration**

[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Tests](https://img.shields.io/badge/tests-passing-green.svg)](#testing)

*Built on HuggingFace's smolagents framework with DeepSeek Chat integration*

</div>

---

## 🚀 Overview

SmolCC is a sophisticated yet lightweight command-line code assistant that combines the power of Large Language Models with a comprehensive suite of development tools. Whether you're exploring codebases, refactoring code, running tests, or managing files, SmolCC provides an intelligent interface that understands context and executes tasks efficiently.

### ✨ Key Features

- **🧠 Intelligent Code Understanding** - Deep codebase analysis and context-aware responses
- **🛠️ Comprehensive Tool Suite** - File operations, search, shell commands, and more
- **🖥️ Cross-Platform Support** - Works seamlessly on Windows (PowerShell) and Unix (Bash)
- **⚡ Interactive & Batch Modes** - Flexible usage patterns for different workflows
- **🔍 Advanced Search Capabilities** - Regex-powered content search and glob pattern matching
- **📁 Smart Directory Management** - Context-aware file and directory operations
- **🔒 Security-First Design** - Built-in command filtering and safety measures
- **🧪 Comprehensive Testing** - 43 unit tests ensuring reliability across platforms

## 🏗️ Architecture

SmolCC leverages a modular architecture built around three core components:

```
┌─────────────────┐    ┌──────────────────┐    ┌─────────────────┐
│   CLI Interface │    │   Agent Core     │    │   Tool System   │
│                 │───▶│                  │───▶│                 │
│ • Interactive   │    │ • DeepSeek Chat  │    │ • Platform-     │
│ • Single Query  │    │ • LiteLLM        │    │   specific      │
│ • Directory     │    │ • Context Mgmt   │    │ • Extensible    │
│   Context       │    │ • System Prompt  │    │ • Type-safe     │
└─────────────────┘    └──────────────────┘    └─────────────────┘
```

### 🔧 Available Tools

| Tool | Platform | Description | Use Cases |
|------|----------|-------------|-----------|
| **BashTool** | Unix/Linux | Execute bash commands with persistent sessions | Running scripts, git operations, system commands |
| **PowerShellTool** | Windows | Execute PowerShell commands with safety checks | Windows-specific tasks, administration, file operations |
| **EditTool** | All | Precise file editing with string replacement | Code refactoring, bug fixes, content updates |
| **ViewTool** | All | Read files with line numbers and pagination | Code review, file inspection, content analysis |
| **GrepTool** | All | Advanced regex-based content search | Finding functions, classes, patterns in code |
| **GlobTool** | All | File pattern matching with recursive search | Locating files by name, extension, or path patterns |
| **LSTool** | All | Tree-structured directory listings | Project exploration, file structure analysis |
| **ReplaceTool** | All | Create or completely replace file contents | Template generation, file creation |
| **CDTool** | All | Smart directory navigation with error handling | Workspace navigation, path management |
| **UserInputTool** | All | Interactive user prompts during execution | Confirmation dialogs, parameter collection |

## 📦 Installation

### Prerequisites

- **Python 3.11+** - Modern Python with async support
- **DeepSeek API Key** - Get yours at [DeepSeek Platform](https://platform.deepseek.com/)
- **Git** (optional) - For enhanced git repository features

### Quick Setup

1. **Clone and Navigate**
   ```bash
   git clone https://github.com/fipauli/smolcc.git
   cd smolcc
   ```

2. **Environment Setup**
   ```bash
   # Create virtual environment
   python -m venv venv
   
   # Activate (Unix/Linux/macOS)
   source venv/bin/activate
   
   # Activate (Windows)
   venv\Scripts\activate
   ```

3. **Install Dependencies**
   ```bash
   # Standard installation
   pip install -e .
   
   # Fast installation with uv (recommended)
   pip install uv
   uv pip install -e .
   ```

4. **Configure API Access**
   ```bash
   # Create .env file
   echo "DEEPSEEK_API_KEY=your_api_key_here" > .env
   ```

<summary>🐳 Docker Setup</summary>

```dockerfile
FROM python:3.11-slim

WORKDIR /app
COPY . .
RUN pip install -e .

ENV DEEPSEEK_API_KEY=your_key_here
CMD ["python", "main.py", "-i"]
```
</details>

## 🎯 Usage Guide

### Command-Line Interface

**Single Query Mode**
```bash
# Analyze current directory
python main.py "What files are in this project?"

# Code analysis
python main.py "Find all TODO comments in Python files"

# Refactoring assistance
python main.py "Rename the function 'old_name' to 'new_name' in utils.py"
```

**Interactive Mode**
```bash
# Start interactive session
python main.py -i

# Session in specific directory
python main.py --cwd /path/to/project -i
```

**Directory-Specific Operations**
```bash
# Run query in specific directory
python main.py --cwd ./src "List all TypeScript files"

# Automatic context switching
python main.py --cwd ~/projects/myapp "Run the test suite"
```

### 💡 Example Use Cases

<details>
<summary>🔍 <strong>Codebase Exploration</strong></summary>

```bash
# Understand project structure
> "Analyze this codebase and explain its architecture"

# Find specific implementations
> "Where is the user authentication logic implemented?"

# Locate configuration files
> "Find all configuration files in this project"
```
</details>

<details>
<summary>🛠️ <strong>Development Tasks</strong></summary>

```bash
# Refactoring
> "Rename all instances of 'getUserData' to 'fetchUserProfile'"

# Bug fixing
> "Find and fix the syntax error in main.py"

# Code quality
> "Add type hints to all functions in the utils module"
```
</details>

<details>
<summary>🧪 <strong>Testing & CI/CD</strong></summary>

```bash
# Run tests
> "Execute the test suite and show results"

# Check code quality
> "Run linting and type checking"

# Build processes
> "Build the project and handle any errors"
```
</details>

<details>
<summary>📁 <strong>File Management</strong></summary>

```bash
# Bulk operations
> "Create a .gitignore file for a Python project"

# Content generation
> "Generate a basic setup.py file for this package"

# Documentation
> "Create API documentation for all public functions"
```
</details>

### 🎛️ Advanced Features

**Memory & Context Management**
- SmolCC automatically looks for `SMOLCC.md` files to maintain project-specific context
- Stores common commands, style preferences, and project insights
- Persistent session memory for complex multi-step tasks

**Smart Command Recognition**
```bash
# These all work naturally:
> "ls"                    # Lists current directory
> "dir"                   # Windows directory listing  
> "git status"            # Git repository status
> "npm test"              # Run Node.js tests
> "pytest"               # Run Python tests
```

**Safety Features**
- Automatic command validation and safety checks
- Banned command filtering (prevents dangerous operations)
- Confirmation prompts for destructive actions
- Sandbox-aware execution environment

## 🧪 Testing

SmolCC includes a comprehensive test suite covering all tools and platforms:

```bash
# Run all tests
python smolcc/run_tool_tests.py

# Run specific tool tests
python smolcc/run_tool_tests.py --tool bash

# Verbose output
python smolcc/run_tool_tests.py --verbose

# Alternative test runner
python -m unittest discover smolcc/tools/tests/
```

**Test Coverage**
- ✅ 43 total tests across all tools
- ✅ Cross-platform compatibility testing
- ✅ Error handling and edge cases
- ✅ Security and safety feature validation
- ✅ Performance and timeout testing

## 🏛️ Project Structure

```
smolcc/
├── 📁 smolcc/                    # Core package
│   ├── 🔧 agent.py              # Agent creation and tool loading
│   ├── 📝 system_prompt.py      # Dynamic prompt generation
│   ├── 📄 system_message.txt    # Base system message template
│   └── 🛠️ tools/               # Tool implementations
│       ├── 🐚 bash_tool.py      # Unix shell commands
│       ├── 💻 powershell_tool.py # Windows shell commands
│       ├── ✏️ edit_tool.py       # File editing
│       ├── 👀 view_tool.py       # File reading
│       ├── 🔍 grep_tool.py       # Content search
│       ├── 📂 glob_tool.py       # File pattern matching
│       ├── 📋 ls_tool.py         # Directory listing
│       ├── 📝 replace_tool.py    # File creation/replacement
│       ├── 📁 cd_tool.py         # Directory navigation
│       ├── 💬 user_input_tool.py # User interaction
│       └── 🧪 tests/            # Comprehensive test suite
├── 🚀 main.py                   # CLI entry point
├── ⚙️ pyproject.toml            # Project configuration
├── 📋 requirements.txt          # Dependencies
├── 📖 README.md                 # This file
├── 📄 LICENSE                   # MIT License
└── 🔧 CLAUDE.md                 # Development guidelines
```

## 🔧 Configuration

### Environment Variables

| Variable | Required | Description | Default |
|----------|----------|-------------|---------|
| `DEEPSEEK_API_KEY` | ✅ | DeepSeek Chat API key | None |

### Project Memory (SMOLCC.md)

SmolCC automatically creates and maintains a `SMOLCC.md` file in your project root to store:

- **Common Commands** - Build, test, lint commands for quick reuse
- **Style Preferences** - Coding conventions and formatting rules  
- **Project Context** - Architecture notes and important insights
- **Custom Tools** - Project-specific automation scripts

Example `SMOLCC.md`:
```markdown
# Project: MyApp

## Common Commands
- Build: `npm run build`
- Test: `npm test`
- Lint: `npm run lint`

## Style Guide
- Use TypeScript strict mode
- Prefer functional components
- Follow Airbnb ESLint config

## Architecture Notes
- Uses React + TypeScript + Vite
- State management with Zustand
- API layer in src/services/
```

## 🐛 Troubleshooting

<details>
<summary><strong>Common Issues</strong></summary>

**API Key Issues**
```bash
# Verify API key is set
echo $DEEPSEEK_API_KEY  # Unix
echo %DEEPSEEK_API_KEY% # Windows

# Test API connectivity
python -c "import os; print('Key found' if os.getenv('DEEPSEEK_API_KEY') else 'Key missing')"
```

**Tool Loading Failures**
```bash
# Check tool imports
python -c "from smolcc.agent import get_available_tools; print(len(get_available_tools()))"

# Verbose tool loading
python main.py "test" --verbose
```

**Permission Errors**
```bash
# Fix file permissions
chmod +x main.py

# Run with elevated privileges (if needed)
sudo python main.py "system command"
```
</details>

<details>
<summary><strong>Platform-Specific Notes</strong></summary>

**Windows**
- PowerShell execution policy may need adjustment
- Use `py` instead of `python` if needed
- Some bash tools won't work (expected behavior)

**macOS**
- May need to install Python via Homebrew
- Bash tool requires bash (not zsh) in some cases

**Linux**
- All tools should work out of the box
- Ensure bash is available at `/bin/bash`
</details>


## 🔗 Related Projects

- [smolagents](https://github.com/huggingface/smolagents) - The underlying agent framework
- [DeepSeek Chat](https://platform.deepseek.com/) - The LLM provider
- [LiteLLM](https://github.com/BerriAI/litellm) - Multi-provider LLM interface

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **HuggingFace** for the excellent smolagents framework
- **DeepSeek** for providing powerful and affordable LLM APIs
- **The Python Community** for the amazing ecosystem of tools and libraries

---