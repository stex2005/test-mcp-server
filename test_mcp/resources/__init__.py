"""Test MCP Resources."""

from fastmcp import FastMCP


def register_all_resources(mcp: FastMCP, **kwargs) -> None:
    """Register all test resources with the MCP server."""

    @mcp.resource("test://info")
    def test_info() -> str:
        """Return information about the test MCP server."""
        return "This is a test MCP server for testing submodule integration."
