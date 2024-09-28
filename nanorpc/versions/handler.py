from enum import IntEnum
from nanorpc.versions import nano_to
from typing import Dict, Any

import importlib


class NodeVersion(IntEnum):
    # version modules need follow strict naming convention
    NANO_TO = 999
    V23_3 = 1  # v23_3.py
    V24_0 = 2  # v24_0.py
    V25_0 = 3  # v25_0.py
    V25_1 = 4  # no changes
    V26_0 = 5  # no changes
    V26_1 = 6  # no changes
    UNDOCUMENTED = 7  # undocumented.py
    V27_1 = 8  # v27_1.py


def _import_version_module(version: NodeVersion) -> Any:
    module_name = f'nanorpc.versions.{version.name.lower()}'
    try:
        return importlib.import_module(module_name)
    except ImportError:
        return None


def _update_commands(commands: Dict[str, Any], module: Any) -> None:
    if module:
        commands.update(getattr(module, 'COMMANDS', {}))
        for command in getattr(module, 'REMOVALS', []):
            commands.pop(command, None)


def get_commands_for_version(node_version: NodeVersion) -> Dict[str, Any]:
    if node_version == NodeVersion.NANO_TO:
        return nano_to.COMMANDS

    commands = {}
    for version in NodeVersion:
        if version > node_version:
            continue

        module = _import_version_module(version)
        _update_commands(commands, module)

    return commands
