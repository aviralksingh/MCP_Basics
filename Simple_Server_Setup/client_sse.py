import asyncio
import nest_asyncio
from mcp import ClientSession
from mcp.client.sse import sse_client

nest_asyncio.apply()

async def main():
    async with sse_client("http://localhost:8050/sse") as (read_stream, write_stream):
        async with ClientSession(read_stream, write_stream) as session:
            await session.initialize()

            tools_result = await session.list_tools()
            print("Available tools:")
            for tool in tools_result.tools:
                print(f"- {tool.name}: {tool.description}")

            result = await session.call_tool("add", arguments={"a": 1, "b": 2})
            print(result)

            result = await session.call_tool("subtract", arguments={"a": 10, "b": 3})
            print(result)

if __name__ == "__main__":
    asyncio.run(main())
