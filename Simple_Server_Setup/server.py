from mcp.server.fastmcp import FastMCP
from dotenv import load_dotenv

load_dotenv("../.env")


mcp = FastMCP(
    name="simple-server-setup",
    host="0.0.0.0",
    port=8050,
    version="0.1.0",
    description="A simple MCP server setup",
    author="Aviral Singh",
    url="https://github.com/aviral-singh/mcp-basics",
    license="MIT",
)

@mcp.tool()
def add(a: int, b: int) -> int:
    return a + b

@mcp.tool()
def subtract(a: int, b: int) -> int:
    return a - b

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="MCP Server Transport Configuration")
    parser.add_argument("--transport", choices=["stdio", "sse"], default="sse",
                       help="Transport mechanism to use (default: sse)")
    args = parser.parse_args()
    transport = args.transport
    if transport=="stdio":
        print("Starting MCP server in stdio mode")
        mcp.run(transport="stdio")
    elif transport=="sse":
        print("Starting MCP server in SSE mode")
        mcp.run(transport="sse")
    else:
        print("Invalid transport")
        exit(1)
