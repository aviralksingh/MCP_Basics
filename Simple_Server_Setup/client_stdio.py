import asyncio
import nest_asyncio
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client
import os
nest_asyncio.apply()

async def main():
    server_params = StdioServerParameters(
        command="python",
        args=["server.py", "--transport", "stdio"],
        env={"PYTHONPATH": "."},
        cwd=os.path.dirname(os.path.abspath(__file__)),
    )
    async with stdio_client(server_params) as (read_stream, write_stream):
        async with ClientSession(read_stream, write_stream) as session:
            await session.initialize()

            tools_result = await session.list_tools()
            print("Available tools:")
            for tool in tools_result.tools:
                print(f"- {tool.name}: {tool.description}")

            print("Connected to MCP server")

            result = await session.call_tool("add", arguments={"a": 1, "b": 2})
            print(result)

            result = await session.call_tool("subtract", arguments={"a": 10, "b": 3})
            print(result)

if __name__ == "__main__":
    asyncio.run(main())
