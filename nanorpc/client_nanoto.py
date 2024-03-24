from nanorpc.client_dynamic import NanoRpc, NodeVersion


class NanoToRpcTyped:
    def __init__(self, auth_key, app_name="nanoto_python_lib", app_email=None, wrap_json=False):
        self.rpc = NanoRpc(url="https://rpc.nano.to",
                           auth_key=auth_key, app_name=app_name, app_email=app_email, node_version=NodeVersion.NANO_TO, wrap_json=wrap_json)

    async def version(self, ):
        return await self.rpc.version()

    async def account_info(self, account, representative=None, weight=None, receivable=None, include_confirmed=None):
        return await self.rpc.account_info(account, representative=representative, weight=weight, receivable=receivable, include_confirmed=include_confirmed)

    async def receivable(self, account, count=None, threshold=None, source=None, include_active=None, min_version=None, sorting=None, include_only_confirmed=None, offset=None, array=None):
        return await self.rpc.receivable(account, count=count, threshold=threshold, source=source, include_active=include_active, min_version=min_version, sorting=sorting, include_only_confirmed=include_only_confirmed, offset=offset, array=array)

    async def account_balance(self, account):
        return await self.rpc.account_balance(account)

    async def account_history(self, account, count=None, raw=None, head=None, offset=None, reverse=None, account_filter=None):
        return await self.rpc.account_history(account, count=count, raw=raw, head=head, offset=offset, reverse=reverse, account_filter=account_filter)

    async def accounts_balances(self, accounts, include_only_confirmed=None):
        return await self.rpc.accounts_balances(accounts, include_only_confirmed=include_only_confirmed)

    async def accounts_receivable(self, accounts, count=None, threshold=None, source=None, include_active=None, sorting=None, include_only_confirmed=None):
        return await self.rpc.accounts_receivable(accounts, count=count, threshold=threshold, source=source, include_active=include_active, sorting=sorting, include_only_confirmed=include_only_confirmed)

    async def block_info(self, hash, json_block=None):
        return await self.rpc.block_info(hash, json_block=json_block)

    async def blocks_info(self, hashes, json_block=None, receivable=None, pending=None, source=None, receive_hash=None, include_not_found=None):
        return await self.rpc.blocks_info(hashes, json_block=json_block, receivable=receivable, pending=pending, source=source, receive_hash=receive_hash, include_not_found=include_not_found)

    async def process(self, block, force=None, subtype=None, json_block=None, async_=None):
        return await self.rpc.process(block, force=force, subtype=subtype, json_block=json_block, async_=async_)

    async def work_generate(self, hash, key=None):
        return await self.rpc.work_generate(hash, key=key)

    async def block_count(self, include_cemented=None):
        return await self.rpc.block_count(include_cemented=include_cemented)

    async def account_key(self, account):
        return await self.rpc.account_key(account)

    async def price(self, currency):
        return await self.rpc.price(currency)

    async def reps(self, ):
        return await self.rpc.reps()

    async def rep_info(self, account):
        return await self.rpc.rep_info(account)

    async def nano_to_raw(self, amount):
        return await self.rpc.nano_to_raw(amount)

    async def raw_to_nano(self, amount):
        return await self.rpc.raw_to_nano(amount)

    async def known(self, ):
        return await self.rpc.known()

    async def aliases(self, ):
        return await self.rpc.aliases()

    async def get_name(self, name):
        return await self.rpc.get_name(name)

    async def update_name(self, name):
        return await self.rpc.update_name(name)

    async def checkout(self, address, amount=None, title=None, webhook=None, notify=None):
        return await self.rpc.checkout(address, amount=amount, title=title, webhook=webhook, notify=notify)

    async def market_data(self, ):
        return await self.rpc.market_data()

    async def nano_swap(self, amount, from_, to, address, refund_address):
        return await self.rpc.nano_swap(amount, from_, to, address, refund_address)

    async def nano_ai(self, model, prompt):
        return await self.rpc.nano_ai(model, prompt)

    async def cloud_wallet(self, refund_address, vanity, password):
        return await self.rpc.cloud_wallet(refund_address, vanity, password)

    async def nano_email(self, amount, email_address, refund_address, claimed_webhook, refunded_webhook):
        return await self.rpc.nano_email(amount, email_address, refund_address, claimed_webhook, refunded_webhook)

    async def buy_rpc(self, email):
        return await self.rpc.buy_rpc(email)

    async def gpu_key(self, email):
        return await self.rpc.gpu_key(email)
