from enum import IntEnum
from nanorpc.versions import nano_to

import importlib


class NodeVersion(IntEnum):
    # version modules need follow strict naming convention
    NANO_TO = -10
    V23_3 = 1  # v23_3.py
    V24_0 = 2  # v24_0.py
    V25_0 = 3  # v25_0.py
    V25_1 = 4  # no changes
    V26_0 = 5  # no changes


def get_commands_for_version(node_version):
    commands = {}

    if node_version == NodeVersion.NANO_TO:
        return nano_to.COMMANDS
    # Apply changes for each version from v23_3 up to the selected version
    for version in NodeVersion:
        if version <= node_version:
            module_name = f'nanorpc.versions.{version.name.lower()}'
            try:
                module = importlib.import_module(module_name)
                version_commands = getattr(module, 'COMMANDS', {})
                commands.update(version_commands)
            except ImportError:
                # If a specific version module doesn't exist, just continue
                continue

    return commands
