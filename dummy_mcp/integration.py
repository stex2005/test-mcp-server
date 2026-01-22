"""Integration module for dummy-mcp with robotmcp_server.

This module provides the register() function called by submodule_integration.py.
"""

import logging

from fastmcp import FastMCP

from dummy_mcp.prompts import register_all_prompts
from dummy_mcp.resources import register_all_resources
from dummy_mcp.tools import register_all_tools

logger = logging.getLogger(__name__)


def register(mcp: FastMCP, **kwargs) -> None:
    """Register all dummy MCP tools, resources, and prompts.

    This is the main entry point called by submodule_integration.py.

    Args:
        mcp: FastMCP instance to register with
        **kwargs: Ignored (for forward compatibility)
    """
    logger.info("[DUMMY_MCP] Initializing dummy-mcp integration")

    # Register all components
    register_all_tools(mcp)
    register_all_resources(mcp)
    register_all_prompts(mcp)

    logger.info("[DUMMY_MCP] Registration complete")
