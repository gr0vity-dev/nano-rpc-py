# NanoRPC

NanoRPC is a Python library for interacting with Nano cryptocurrency nodes via their JSON-RPC API. It provides an easy-to-use interface to execute RPC (Remote Procedure Call) commands supported by different versions of Nano nodes.

## Features

- Compatible with Python 3.7 and higher.
- Supports asynchronous operations using `asyncio` and `aiohttp`.
- Automatically adjusts available RPC methods based on the version of the connected Nano node.
- Provides a simple and intuitive API for executing RPC commands.

## Requirements

- Python 3.7 and higher
- aiohttp library

## Installation

You can install NanoRPC using `pip`:

```bash
pip install nanorpc
```

## Usage

Here's a basic example of how to use NanoRPC to interact with a Nano node:

```python
import asyncio
from nanorpc import NanoRpc, NodeVersion

async def main():
    # Connect to a Nano node
    rpc = NanoRpc(url='http://localhost:7076', node_version=NodeVersion.V25_0)

    # Execute an RPC command
    block_count = await rpc.block_count()
    print(f"Current block count: {block_count}")

    # Execute another RPC command
    version_info = await rpc.version()
    print(f"Node version: {version_info}")

# Run the main function within an asyncio event loop
asyncio.run(main())
```

### Error Handling

NanoRPC includes several error handling mechanisms. If an RPC command fails or if a network issue is encountered, the library will retry the request for a specified number of times. If all retries are exhausted, the library will raise a `MaxRetriesExceededError`.

### Available RPC Commands

NanoRPC provides access to various RPC commands based on the connected Nano node version. For a complete list of available commands and their parameters, please refer to the [versions folder](./nanorpc/versions) in this repository.

### Official RPC Documentation

For detailed documentation on the Nano RPC protocol and available commands, please visit the [Nano RPC Documentation](https://docs.nano.org/commands/rpc-protocol/) page.

## Contributing

Contributions to NanoRPC are welcome! If you find any issues, have suggestions, or would like to contribute enhancements or new features, please open an issue or submit a pull request.

## License

NanoRPC is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.
