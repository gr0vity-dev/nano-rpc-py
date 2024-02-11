import nano_lib_py as nl

# private methods not to use directly


def nl_raw_to_nano(amount):
    return nl.convert(amount, "raw", "nano")


def nl_nano_to_raw(amount):
    return nl.convert(amount, "nano", "raw")


def nl_int_balance(balance):
    return int(str(balance))


def _get_link_as_hash(link):
    return nl.get_account_public_key(account_id=link) if str(link).startswith("nano_") else link


def nl_generate_seed():
    return nl.generate_seed()


def nl_get_private_key_from_seed(seed, seed_index):
    return nl.generate_account_private_key(seed, seed_index)


def nl_get_account_from_seed(seed, seed_index):
    return nl.generate_account_id(seed, seed_index)


def nl_get_account_from_key(private_key):
    return nl.get_account_id(private_key=private_key)


def nl_get_account_public_key(account):
    return nl.get_account_public_key(account_id=account)


def nl_create_block_from_key(private_key, previous, balance, link, work, representative, difficulty):
    account = nl_get_account_from_key(private_key)
    block = nl.Block(
        block_type="state",
        account=account,
        previous=previous,
        balance=int(str(balance)),
        representative=representative,
        link=_get_link_as_hash(link),
        work=work,
        difficulty=difficulty
    )
    block.sign(private_key)
    return block.json()
