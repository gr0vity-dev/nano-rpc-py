### Deprecated Commands
# accounts_pending
# pending
# pending_exists
# search_pending
# search_pending_all
# wallet_pending

### New Commands
# populate_backlog
# accounts_receivable   (replaces accounts_pending)
# receivable            (replaces pending)
# receivable_exists     (replaces pending_exists)
# search_receivable     (replaces search_pending)
# search_receivable_all (replaces search_pending_all)
# wallet_receivable     (replaces wallet_pending)

### Changed Commands
# account_info (added optional 'receivable')
# blocks_info (added optional 'receivable')
# ledger (added optional 'receivable')
# wallet_ledger (added optional 'receivable')

CHANGES = {
    "account_info": {
        "required": ["account"],
        "optional": [
            "representative", "weight", "receivable", "pending",
            "include_confirmed"
        ]
    },
    "accounts_pending": {
        "deprecated":
        True,
        "required": ["accounts", "count"],
        "optional": [
            "threshold", "source", "include_active", "sorting",
            "include_only_confirmed"
        ]
    },
    "accounts_receivable": {
        "required": ["accounts", "count"],
        "optional": [
            "threshold", "source", "include_active", "sorting",
            "include_only_confirmed"
        ]
    },
    "blocks_info": {
        "required": ["hashes"],
        "optional": [
            "json_block", "receivable", "pending", "source", "receive_hash",
            "include_not_found"
        ]
    },
    "ledger": {
        "required": ["account", "count"],
        "optional": [
            "representative", "weight", "receivable", "pending",
            "modified_since", "sorting", "threshold"
        ]
    },
    "pending": {
        "deprecated":
        True,
        "required": ["account", "count"],
        "optional": [
            "count", "threshold", "source", "include_active", "min_version",
            "sorting", "include_only_confirmed"
        ]
    },
    "pending_exists": {
        "deprecated": True,
        "required": ["hash"],
        "optional": ["include_active", "include_only_confirmed"]
    },
    "populate_backlog": {
        "required": [],
        "optional": []
    },
    "receivable": {
        "required": ["account", "count"],
        "optional": [
            "count", "threshold", "source", "include_active", "min_version",
            "sorting", "include_only_confirmed", "offset"
        ]
    },
    "receivable_exists": {
        "required": ["hash"],
        "optional": ["include_active", "include_only_confirmed"]
    },
    "search_receivable": {
        "required": ["wallet"],
        "optional": []
    },
    "search_receivable_all": {
        "required": [],
        "optional": []
    },
    "search_pending": {
        "deprecated": True,
        "required": ["wallet"],
        "optional": []
    },
    "search_pending_all": {
        "deprecated": True,
        "required": [],
        "optional": []
    },
    "wallet_pending": {
        "deprecated": True,
        "required": ["wallet"],
        "optional": ["count", "threshold", "source"]
    },
    "wallet_receivable": {
        "required": ["wallet"],
        "optional": ["count", "threshold", "source"]
    },
    "wallet_ledger": {
        "required": ["wallet"],
        "optional": ["representative", "weight", "receivable", "pending"]
    },
}
