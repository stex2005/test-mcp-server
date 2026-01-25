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
├── README.md                   # This file
├── .gitignore                  # Git ignore patterns
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

## Installation

### Via robotmcp-server CLI (Recommended)

```bash
robotmcp-server add https://github.com/robotmcp/test-mcp-server.git
```

This automatically:
- Clones the repository as a git submodule
- Installs dependencies from `pyproject.toml`
- Registers tools via `test_mcp/integration.py`

To verify installation:

```bash
robotmcp-server list        # Show installed modules
robotmcp-server list-tools  # Show available tools
```

To remove:

```bash
robotmcp-server remove test-mcp-server
```

### Standalone Installation

```bash
git clone https://github.com/robotmcp/test-mcp-server.git
cd test-mcp-server
pip install -e .
```

## Usage

### With robotmcp-server

Once installed, tools are automatically registered. Verify with:

```bash
robotmcp-server list-tools
```

Expected output:
```
test_mcp:
  - ping: Simple ping tool to test connectivity.
  - greet: Greet a person by name.
```

### Standalone

```python
from fastmcp import FastMCP
from test_mcp.integration import register

mcp = FastMCP("test-server")
register(mcp)
```

## Integration Pattern

The `integration.py` module provides the `register(mcp, **kwargs)` function called by robotmcp_server's submodule auto-discovery:

```python
# test_mcp/integration.py
def register(mcp: FastMCP, **kwargs) -> None:
    """Register all test MCP tools, resources, and prompts."""
    register_all_tools(mcp)
    register_all_resources(mcp)
    register_all_prompts(mcp)
```

This pattern allows robotmcp_server to dynamically load and register components from submodules.

## Development

### Requirements

- Python >= 3.10
- fastmcp >= 2.11.3

### Setup

```bash
# Clone the repository
git clone https://github.com/robotmcp/test-mcp-server.git
cd test-mcp-server

# Install in development mode
pip install -e .
```

### Adding New Tools

1. Add tool functions to `test_mcp/tools/tools.py`
2. Use the `@mcp.tool()` decorator to register them
3. Test with `robotmcp-server list-tools`

### Testing with robotmcp-server

For local development, you can add directly from a local path:

```bash
# From the robotmcp_server directory
git submodule add ../path/to/test-mcp-server
robotmcp-server list-tools
```

## License

Copyright (c) 2025 Contoro. All rights reserved.
