"""Dummy MCP Tools."""

from fastmcp import FastMCP


def register_all_tools(mcp: FastMCP, **kwargs) -> None:
    """Register all dummy tools with the MCP server."""

    @mcp.tool(description="A dummy tool that says hello. Used to test submodule integration.")
    def dummy_hello(name: str = "World") -> dict:
        """Say hello to someone.

        Args:
            name: The name to greet.

        Returns:
            dict: A greeting message.
        """
        return {"message": f"Hello, {name}! This is from dummy-mcp-server."}

    @mcp.tool(description="Add two numbers together. A simple test tool.")
    def dummy_add(a: int, b: int) -> dict:
        """Add two numbers.

        Args:
            a: First number.
            b: Second number.

        Returns:
            dict: The sum of the two numbers.
        """
        return {"result": a + b, "expression": f"{a} + {b} = {a + b}"}
