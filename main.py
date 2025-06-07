import sys
import os
import argparse
from smolcc import create_agent
from smolcc.agent import refresh_agent_context

def print_welcome():
    """Print welcome message with usage information."""
    print("🤖 Welcome to SmolCC - A Smart Code Assistant")
    print("=" * 50)
    print()
    print("SmolCC is a lightweight code assistant powered by DeepSeek Chat")
    print("with intelligent tool-using capabilities for file operations,")
    print("code analysis, and project management.")
    print()
    print("📋 USAGE:")
    print("  python main.py \"your question\"        # Ask a single question")
    print("  python main.py -i                      # Interactive mode")
    print("  python main.py --cwd /path \"question\"  # Set working directory")
    print()
    print("🛠️  AVAILABLE TOOLS:")
    print("  • File Operations: read, edit, create files")
    print("  • Directory Management: list, navigate, change working directory")
    print("  • Code Search: find files, search content with regex")
    print("  • Shell Commands: execute bash/PowerShell commands")
    print("  • Project Analysis: understand code structure and patterns")
    print()
    print("💡 EXAMPLE QUERIES:")
    print('  "What files are in the current directory?"')
    print('  "Find all Python files containing TODO comments"')
    print('  "Create a new README.md file for this project"')
    print('  "Change to the src directory and list its contents"')
    print('  "Run the tests and show me the results"')
    print()
    print("🔧 COMMAND LINE OPTIONS:")
    print("  -i, --interactive    Start interactive mode for multiple queries")
    print("  --cwd PATH          Set the working directory for the agent")
    print("  -h, --help          Show detailed help message")
    print()
    print("🚀 To get started, try: python main.py -i")
    print("=" * 50)

def main():
    """
    Main entry point for SmolCC.
    Handles command line arguments and runs the agent.
    """
    parser = argparse.ArgumentParser(
        description="SmolCC - A lightweight code assistant with tools",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python main.py "What files are in this directory?"
  python main.py -i
  python main.py --cwd /path/to/project "analyze this codebase"
  
For more information, visit: https://github.com/aniemerg/smolcc
        """
    )
    parser.add_argument("query", nargs="*", help="Query to send to the assistant")
    parser.add_argument("-i", "--interactive", action="store_true", 
                        help="Run in interactive mode (prompt for queries)")
    parser.add_argument("--cwd", help="Set the working directory for the agent")
    
    args = parser.parse_args()
    
    # Show welcome message if no arguments are provided at all
    if len(sys.argv) == 1:
        print_welcome()
        return
    
    # Set the working directory if provided
    working_dir = args.cwd if args.cwd else os.getcwd()
    
    # Actually change to the working directory if specified
    if args.cwd:
        try:
            os.chdir(working_dir)
            print(f"📁 Changed to working directory: {working_dir}")
        except (FileNotFoundError, PermissionError) as e:
            print(f"❌ Error: Cannot change to directory '{working_dir}': {e}")
            return
    
    # Create the agent with the appropriate working directory
    print("🔧 Initializing SmolCC agent...")
    agent = create_agent(os.getcwd()) # Use os.getcwd() as we've already chdir'd
    print(f"📁 Working directory: {os.getcwd()}")
    print()
    
    # Handle the query based on arguments
    if args.query:
        query = " ".join(args.query)
        print(f"❓ Query: {query}")
        print("🤔 Processing...")
        print()
        result = agent.run(query)
        print("📋 Response:")
        print(result)
    else:
        # If no query is provided, default to interactive mode.
        # This covers `main.py -i` and `main.py --cwd /some/path`.
        run_interactive_mode(agent)

def recreate_agent_with_cwd(new_cwd, current_agent=None):
    """Recreate the agent with a new working directory and updated context."""
    try:
        os.chdir(new_cwd)
        print(f"📁 Changed to working directory: {os.getcwd()}")
        
        # Try to use the more efficient refresh method if agent is provided
        if current_agent is not None:
            print("🔄 Refreshing agent context...")
            updated_agent = refresh_agent_context(current_agent, os.getcwd())
            print("✅ Agent context refreshed successfully")
            return updated_agent
        else:
            # Fallback to full recreation
            print("🔄 Creating new agent with directory context...")
            agent = create_agent(os.getcwd())
            print("✅ Agent context updated successfully")
            return agent
    except (FileNotFoundError, PermissionError) as e:
        print(f"❌ Error: Cannot change to directory '{new_cwd}': {e}")
        return None

def run_interactive_mode(agent):
    """Run SmolCC in interactive mode, prompting for queries."""
    print("🚀 SmolCC Interactive Mode")
    print("=" * 40)
    print("💬 Enter your queries and I'll help you with:")
    print("   • File operations and code analysis")
    print("   • Directory navigation and management") 
    print("   • Shell commands and project tasks")
    print()
    print("💡 Useful commands:")
    print('   "help" - Show available tools and capabilities')
    print('   "cd <path>" - Change working directory (updates agent context)')
    print('   "ls" or "dir" - List current directory contents')
    print()
    print("🔚 Type 'exit', 'quit', or press Ctrl+C to end")
    print("=" * 40)
    
    while True:
        try:
            query = input("\n🤖 SmolCC> ")
            if query.lower() in ("exit", "quit"):
                print("👋 Goodbye! Thanks for using SmolCC!")
                break
            
            if not query.strip():
                continue
            
            # Handle special built-in commands
            if query.lower() == "help":
                print_help_commands()
                continue
            
            # Handle cd command to change working directory
            if query.strip().lower().startswith("cd "):
                new_path = query.strip()[3:].strip()
                if new_path:
                    # Handle relative paths and expand ~
                    new_path = os.path.expanduser(new_path)
                    if not os.path.isabs(new_path):
                        new_path = os.path.join(os.getcwd(), new_path)
                    new_path = os.path.normpath(new_path)
                    
                    new_agent = recreate_agent_with_cwd(new_path, agent)
                    if new_agent is not None:
                        agent = new_agent
                else:
                    print("❌ Usage: cd <directory_path>")
                continue
                
            print("🤔 Processing...")
            result = agent.run(query)
            print("📋 Response:")
            print(result)
            
        except KeyboardInterrupt:
            print("\n👋 Goodbye! Thanks for using SmolCC!")
            break
        except Exception as e:
            print(f"❌ Error: {e}")

def print_help_commands():
    """Print help information for interactive mode."""
    print("🛠️  Available Tools & Capabilities:")
    print("   📁 File Operations:")
    print("      • Read files: 'show me the contents of main.py'")
    print("      • Edit files: 'add a comment to line 10 in main.py'")
    print("      • Create files: 'create a new config.json file'")
    print()
    print("   📂 Directory Management:")
    print("      • List contents: 'what files are here?'")
    print("      • Change directory: 'cd /path/to/directory' or 'cd to the src folder'")
    print("      • Navigate: 'go to the parent directory'")
    print("      • Note: Use 'cd <path>' for direct directory changes that update agent context")
    print()
    print("   🔍 Code Search & Analysis:")
    print("      • Find files: 'find all Python files'")
    print("      • Search content: 'find TODO comments in the code'")
    print("      • Analyze structure: 'explain this project structure'")
    print()
    print("   ⚡ Shell Commands:")
    print("      • Run tests: 'run the test suite'")
    print("      • Git operations: 'show git status'")
    print("      • Build tools: 'run npm install'")
    print()
    print("   🎯 Natural Language:")
    print("      Just ask naturally! 'How many Python files are in this project?'")
    print("      'Create a simple HTTP server script'")
    print("      'Fix the syntax error in utils.py'")

if __name__ == "__main__":
    main()
