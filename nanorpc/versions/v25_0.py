### Non Backwards compatibale changes
### accounts_balances (in case of any error returns 'errors' instead of 'error')
### accounts_frontiers (in case of any error returns 'errors' instead of 'error')
### accounts_representatives (in case of any error returns 'errors' instead of 'error')

### Changed Commands
# accounts_balances (added optional 'include_only_confirmed')

CHANGES = {
    "accounts_balances": {
        "required": ["accounts"],
        "optional": ["include_only_confirmed"]
    }
}