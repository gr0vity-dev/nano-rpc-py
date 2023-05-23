from . import v23_3, v24_0, v25_0
from enum import IntEnum


class RpcVersionHandler:
    VERSIONS = {
        "V23.3": v23_3.COMMANDS,
        "V24.0": v24_0.CHANGES,
        "V25.0": v25_0.CHANGES
    }


class NodeVersion(IntEnum):
    V23_3 = 1
    V24_0 = 2
    V25_0 = 3


COMMANDS_BASE = v23_3.COMMANDS
COMMANDS_CHANGES = {
    NodeVersion.V23_3: {},
    NodeVersion.V24_0: v24_0.CHANGES,
    NodeVersion.V25_0: v25_0.CHANGES
}
