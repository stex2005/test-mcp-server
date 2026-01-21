"""Dummy MCP Resources."""

from fastmcp import FastMCP


def register_all_resources(mcp: FastMCP, **kwargs) -> None:
    """Register all dummy resources with the MCP server."""

    @mcp.resource("dummy://info")
    def dummy_info() -> str:
        """Return information about the dummy MCP server."""
        return "This is a dummy MCP server for testing submodule integration."
