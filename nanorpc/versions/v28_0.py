COMMANDS = {
    "account_history": {
        "required": ["account", "count"],
        "optional": [
            "raw",
            "head",
            "offset",
            "reverse",
            "account_filter",
            "include_linked_account",  # Added in V28.0
        ],
    },
    "block_info": {
        "required": ["hash"],
        "optional": [
            "json_block",
            "include_linked_account",  # Added in V28.0
        ],
    },
    "blocks_info": {
        "required": ["hashes"],
        "optional": [
            "json_block",
            "pending",  # Retained for backwards compat checking although 'receivable' preferred
            "source",
            "receive_hash",  # Added V24.0
            "include_not_found",  # Added V19.0
            "include_linked_account",  # Added in V28.0
        ],
    },
    "bootstrap_priorities": {
        "required": [],
        "optional": [],
    },
    "bootstrap_reset": {
        "required": [],
        "optional": [],
    },
    "krai_from_raw": {
        "required": ["amount"],
        "optional": [],
        "deprecated": True,
    },
    "krai_to_raw": {
        "required": ["amount"],
        "optional": [],
        "deprecated": True,
    },
    "mrai_from_raw": {
        "required": ["amount"],
        "optional": [],
        "deprecated": True,
    },
    "mrai_to_raw": {
        "required": ["amount"],
        "optional": [],
        "deprecated": True,
    },
    "rai_from_raw": {
        "required": ["amount"],
        "optional": [],
        "deprecated": True,
    },
    "rai_to_raw": {
        "required": ["amount"],
        "optional": [],
        "deprecated": True,
    },
}
REMOVALS = []
