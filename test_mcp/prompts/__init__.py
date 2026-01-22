"""Test MCP Prompts."""

from fastmcp import FastMCP


def register_all_prompts(mcp: FastMCP, **kwargs) -> None:
    """Register all test prompts with the MCP server."""

    @mcp.prompt(description="A test prompt for testing submodule integration.")
    def test_greeting(name: str = "User") -> str:
        """Generate a greeting message.

        Args:
            name: The name to greet.

        Returns:
            str: A greeting prompt.
        """
        return f"Please greet {name} warmly and ask how you can help them today."
