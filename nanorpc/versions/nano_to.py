COMMANDS = {
    "version": {
        "required": [],
        "optional": []
    },
    "account_info": {
        "required": ["account"],
        "optional":
        ["representative", "weight", "receivable", "include_confirmed"]
    },
    "receivable": {
        "required": ["account"],
        "optional": [
            "count", "threshold", "source", "include_active", "min_version",
            "sorting", "include_only_confirmed", "offset", "array"
        ]
    },
    "account_balance": {
        "required": ["account"],
        "optional": []
    },
    "account_history": {
        "required": ["account", ],
        "optional": ["count", "raw", "head", "offset", "reverse", "account_filter"]
    },
    "accounts_balances": {
        "required": ["accounts"],
        "optional": ["include_only_confirmed"]
    },
    "accounts_receivable": {
        "required": ["accounts"],
        "optional": [
            "count", "threshold", "source", "include_active", "sorting",
            "include_only_confirmed"
        ]
    },
    "block_info": {
        "required": ["hash"],
        "optional": ["json_block"]
    },
    "blocks_info": {
        "required": ["hashes"],
        "optional": [
            "json_block", "receivable", "pending", "source", "receive_hash",
            "include_not_found"
        ]
    },
    "process": {
        "required": ["block"],
        "optional": ["force", "subtype", "json_block", "async"]
    },
    "work_generate": {
        "required": ["hash"],
        "optional": ["key"]
    },
    "block_count": {
        "required": [],
        "optional": ["include_cemented"]
    },
    "account_key": {
        "required": ["account"],
        "optional": []
    },
    "price": {
        "required": ["currency"],
        "optional": []
    },
    "reps": {
        "required": [],
        "optional": []
    },
    "rep_info": {
        "required": ["account"],
        "optional": []
    },
    "nano_to_raw": {
        "required": ["amount"],
        "optional": []
    },
    "raw_to_nano": {
        "required": ["amount"],
        "optional": []
    },
    "known": {
        "required": [],
        "optional": []
    },
    "aliases": {
        "required": [],
        "optional": []
    },
    "get_name": {
        "required": ["name"],
        "optional": []
    },
    "update_name": {
        "required": ["name"],
        "optional": []
    },
    "checkout": {
        "required": ["address"],
        "optional": ["amount", "title", "webhook", "notify"]
    },
    "market_data": {
        "required": [],
        "optional": []
    },
    "nano_swap": {
        "required": ["amount", "from", "to", "address", "refund_address"],
        "optional": []
    },
    "nano_ai": {
        "required": ["model", "prompt"],
        "optional": []
    },
    "cloud_wallet": {
        "required": ["refund_address", "vanity", "password"],
        "optional": []
    },
    "nano_email": {
        "required": ["amount", "email_address", "refund_address", "claimed_webhook", "refunded_webhook"],
        "optional": []
    },
    "buy_rpc": {
        "required": ["email"],
        "optional": []
    },
    "gpu_key": {
        "required": ["email"],
        "optional": []
    }
}
