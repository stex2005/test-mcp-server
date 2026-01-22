"""Dummy MCP Tools - Tool implementations.

This module provides the main registration function to register all dummy MCP tools
with a FastMCP instance.
"""

from fastmcp import FastMCP

from dummy_mcp.tools.tools import register_tools


def register_all_tools(mcp: FastMCP, **kwargs) -> None:
    """Register all dummy MCP tools with the provided FastMCP instance.

    Args:
        mcp: FastMCP instance to register tools with
        **kwargs: Ignored (for forward compatibility)
    """
    register_tools(mcp)
