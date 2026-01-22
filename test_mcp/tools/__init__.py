"""Test MCP Tools - Tool implementations.

This module provides the main registration function to register all test MCP tools
with a FastMCP instance.
"""

from fastmcp import FastMCP

from test_mcp.tools.tools import register_tools


def register_all_tools(mcp: FastMCP, **kwargs) -> None:
    """Register all test MCP tools with the provided FastMCP instance.

    Args:
        mcp: FastMCP instance to register tools with
        **kwargs: Ignored (for forward compatibility)
    """
    register_tools(mcp)
