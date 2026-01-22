"""Integration module for test-mcp with robotmcp_server.

This module provides the register() function called by submodule_integration.py.
"""

import logging

from fastmcp import FastMCP

from test_mcp.prompts import register_all_prompts
from test_mcp.resources import register_all_resources
from test_mcp.tools import register_all_tools

logger = logging.getLogger(__name__)


def register(mcp: FastMCP, **kwargs) -> None:
    """Register all test MCP tools, resources, and prompts.

    This is the main entry point called by submodule_integration.py.

    Args:
        mcp: FastMCP instance to register with
        **kwargs: Ignored (for forward compatibility)
    """
    logger.info("[TEST_MCP] Initializing test-mcp integration")

    # Register all components
    register_all_tools(mcp)
    register_all_resources(mcp)
    register_all_prompts(mcp)

    logger.info("[TEST_MCP] Registration complete")
