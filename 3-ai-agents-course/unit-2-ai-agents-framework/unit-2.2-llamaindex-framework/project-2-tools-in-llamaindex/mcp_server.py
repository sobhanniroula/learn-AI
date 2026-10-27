from mcp.server.mcpserver import MCPServer

mcp = MCPServer("Demo")


@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers."""
    return a + b


@mcp.tool()
def multiply(a: int, b: int) -> int:
    """Multiply two numbers."""
    return a * b


if __name__ == "__main__":
    # SSE server on http://127.0.0.1:8000/sse
    mcp.run(transport="sse", host="127.0.0.1", port=8000)
