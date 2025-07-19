from mcp.client.stdio import stdio_client, StdioServerParameters
from strands import Agent
from strands.tools.mcp.mcp_client import MCPClient
from strands.models import BedrockModel
import sys
import asyncio
import time
import atexit
import signal

def create_stdio_transport():
    server_params = StdioServerParameters(
        command="python",
        args=["server/main.py"],
    )
    return stdio_client(server_params)

# Create enhanced BedrockModel with shared config
bedrock_model = BedrockModel(
    model_id="us.anthropic.claude-3-5-sonnet-20240620-v1:0",
    region_name='us-east-1',
)

stdio_mcp_client = MCPClient(create_stdio_transport)

def cleanup_handler():
    """Clean shutdown handler to avoid transport errors"""
    try:
        # Force close any remaining MCP client connections
        if hasattr(stdio_mcp_client, '_client') and stdio_mcp_client._client:
            stdio_mcp_client._client = None
        time.sleep(0.2)  # Give time for cleanup
    except:
        pass

# Register cleanup handler
atexit.register(cleanup_handler)

try:
    # Use the MCP server in a context manager
    with stdio_mcp_client:
        # Get the tools from the MCP server
        tools = stdio_mcp_client.list_tools_sync()

        # Create an agent with the MCP tools
        agent = Agent(
            tools=tools,
            model=bedrock_model,
        )

        print("Chat started! Type 'exit' or 'quit' to end the conversation.")
        
        while True:
            try:
                user_input = input("\n\nUser: ")
                if user_input.strip().lower() in ["exit", "quit"]:
                    print("Exiting... Goodbye!")
                    break
                response = agent(user_input)
            except KeyboardInterrupt:
                print("\nExiting... Goodbye!")
                break
            except EOFError:
                print("\nExiting... Goodbye!")
                break

except Exception as e:
    print(f"An error occurred: {e}")
finally:
    # Cleanup to avoid transport errors during shutdown
    try:
        # Give the context manager time to properly close
        time.sleep(0.3)
        
        # Suppress stderr temporarily to hide cleanup warnings
        import os
        stderr_fd = sys.stderr.fileno()
        with open(os.devnull, 'w') as devnull:
            old_stderr = os.dup(stderr_fd)
            os.dup2(devnull.fileno(), stderr_fd)
            try:
                # Brief pause for any remaining cleanup
                time.sleep(0.1)
            finally:
                # Restore stderr
                os.dup2(old_stderr, stderr_fd)
                os.close(old_stderr)
                
    except Exception:
        # Suppress any cleanup errors
        pass
    
    # Force exit to avoid any lingering processes
    os._exit(0)