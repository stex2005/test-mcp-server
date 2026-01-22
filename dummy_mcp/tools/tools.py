"""Basic tools for dummy MCP."""

from fastmcp import FastMCP


def register_tools(mcp: FastMCP) -> None:
    """Register basic tools."""

    @mcp.tool(description="Simple ping tool to test connectivity.")
    def ping() -> dict:
        """Ping the server to check if it's alive.

        Returns:
            dict: A pong response.
        """
        return {"message": "pong"}

    @mcp.tool(description="Greet a person by name.")
    def greet(name: str) -> dict:
        """Greet someone by name.

        Args:
            name: The name of the person to greet.

        Returns:
            dict: A greeting message.
        """
        return {"message": f"Hello, {name}!"}
