# Non Backwards compatibale changes
# accounts_balances (in case of any error returns 'errors' instead of 'error')
# accounts_frontiers (in case of any error returns 'errors' instead of 'error')
# accounts_representatives (in case of any error returns 'errors' instead of 'error')

# Changed Commands
# accounts_balances (added optional 'include_only_confirmed')

COMMANDS = {
    "account_count": {
        "required": [],
        "optional": []
    },
    "block": {  # same as block_info
        "required": ["hash"],
        "optional": ["json_block"]
    },
    "debug_bootstrap_priority_info": {
        "required": [],
        "optional": []
    },
    "pruned_exists": {
        "required": ["hash"],
        "optional": []
    },
    "wallet_unlock": {  # same as password_enter
        "required": ["wallet", "password"],
        "optional": []
    },
    "wallet_balance_total": {  # same as wallet_info
        "required": ["wallet"],
        "optional": []
    },
    "wallet_key_valid": {
        "required": ["wallet"],
        "optional": []
    }
}
