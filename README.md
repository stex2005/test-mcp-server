# Test MCP Server

A minimal Model Context Protocol (MCP) server for testing submodule integration with robotmcp_server.

## Features

- **Simple Tools**: `ping` and `greet` for testing MCP connectivity
- **Integration Ready**: Compatible with robotmcp_server's submodule auto-discovery
- **Minimal Dependencies**: Only requires `fastmcp>=2.11.3`

## Project Structure

```
test-mcp-server/
├── pyproject.toml              # Package metadata
└── test_mcp/
    ├── __init__.py             # Package init
    ├── integration.py          # Entry point for robotmcp_server
    ├── tools/
    │   ├── __init__.py         # Tool registration hub
    │   └── tools.py            # Tool implementations
    ├── resources/
    │   └── __init__.py         # Resource registration
    └── prompts/
        └── __init__.py         # Prompt registration
```

## Tools

| Tool | Parameters | Description |
|------|------------|-------------|
| `ping` | None | Returns `{"message": "pong"}` - tests connectivity |
| `greet` | `name: str` | Returns `{"message": "Hello, {name}!"}` |

## Usage with robotmcp_server

Add as a git submodule:

```bash
cd robotmcp_server
git submodule add https://github.com/robotmcp/test-mcp-server.git
git submodule update --init --recursive
```

The server automatically discovers and registers tools via `test_mcp/integration.py`.

## Standalone Usage

```bash
pip install -e .
```

```python
from fastmcp import FastMCP
from test_mcp.integration import register

mcp = FastMCP("test-server")
register(mcp)
```

## Integration Pattern

The `integration.py` module provides the `register(mcp, **kwargs)` function called by robotmcp_server's submodule auto-discovery:

```python
from fastmcp import FastMCP
from test_mcp.integration import register

def register(mcp: FastMCP, **kwargs) -> None:
    """Register all test MCP tools, resources, and prompts."""
    register_all_tools(mcp)
    register_all_resources(mcp)
    register_all_prompts(mcp)
```

## License

Copyright (c) 2025 Contoro. All rights reserved.
