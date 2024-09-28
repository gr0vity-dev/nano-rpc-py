# Non Backwards compatibale changes
# accounts_balances (in case of any error returns 'errors' instead of 'error')
# accounts_frontiers (in case of any error returns 'errors' instead of 'error')
# accounts_representatives (in case of any error returns 'errors' instead of 'error')

# Changed Commands
# accounts_balances (added optional 'include_only_confirmed')

COMMANDS = {
    "election_statistics": {
        "required": [],
        "optional": []
    },
}

REMOVALS = ["confirmation_height_currently_processing"]
