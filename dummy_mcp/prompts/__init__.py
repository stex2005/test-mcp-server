"""Dummy MCP Prompts."""

from fastmcp import FastMCP


def register_all_prompts(mcp: FastMCP, **kwargs) -> None:
    """Register all dummy prompts with the MCP server."""

    @mcp.prompt(description="A dummy prompt for testing submodule integration.")
    def dummy_greeting(name: str = "User") -> str:
        """Generate a greeting message.

        Args:
            name: The name to greet.

        Returns:
            str: A greeting prompt.
        """
        return f"Please greet {name} warmly and ask how you can help them today."
