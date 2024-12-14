from nanorpc.client_dynamic import NanoRpc, NodeVersion


class NanoRpcTyped:
    def __init__(self, url, username=None, password=None, wrap_json=False):
        #
        self.rpc = NanoRpc(url=url, username=username,
                           password=password, node_version=NodeVersion.V27_1, wrap_json=wrap_json)

    async def account_balance(self, account, include_only_confirmed=True):
        return await self.rpc.account_balance(account, include_only_confirmed=include_only_confirmed)

    async def account_block_count(self, account):
        return await self.rpc.account_block_count(account)

    async def account_count(self):
        return await self.rpc.account_count()

    async def account_create(self, wallet, index=None, work=None):
        return await self.rpc.account_create(wallet, index=index, work=work)

    async def account_get(self, key):
        return await self.rpc.account_get(key)

    async def account_history(self, account, count=None, raw=None, head=None, offset=None, reverse=None, account_filter=None):
        return await self.rpc.account_history(account, count=count, raw=raw, head=head, offset=offset, reverse=reverse, account_filter=account_filter)

    async def account_info(self, account, representative=None, weight=None, receivable=None, pending=None, include_confirmed=None):
        return await self.rpc.account_info(account, representative=representative, weight=weight, receivable=receivable, pending=pending, include_confirmed=include_confirmed)

    async def account_key(self, account):
        return await self.rpc.account_key(account)

    async def account_list(self, wallet):
        return await self.rpc.account_list(wallet)

    async def account_move(self, wallet, source, accounts):
        return await self.rpc.account_move(wallet, source, accounts)

    async def account_remove(self, wallet, account):
        return await self.rpc.account_remove(wallet, account)

    async def account_representative(self, account):
        return await self.rpc.account_representative(account)

    async def account_representative_set(self, wallet, account, representative, work=None):
        return await self.rpc.account_representative_set(wallet, account, representative, work=work)

    async def account_weight(self, account):
        return await self.rpc.account_weight(account)

    async def accounts_balances(self, accounts, include_only_confirmed=None):
        return await self.rpc.accounts_balances(accounts, include_only_confirmed=include_only_confirmed)

    async def accounts_create(self, wallet, count, work=None):
        return await self.rpc.accounts_create(wallet, count, work=work)

    async def accounts_frontiers(self, accounts):
        return await self.rpc.accounts_frontiers(accounts)

    async def accounts_pending(self, accounts, count, threshold=None, source=None, include_active=None, sorting=None, include_only_confirmed=None):
        return await self.rpc.accounts_pending(accounts, count, threshold=threshold, source=source, include_active=include_active, sorting=sorting, include_only_confirmed=include_only_confirmed)

    async def accounts_receivable(self, accounts, count, threshold=None, source=None, include_active=None, sorting=None, include_only_confirmed=None):
        return await self.rpc.accounts_receivable(accounts, count, threshold=threshold, source=source, include_active=include_active, sorting=sorting, include_only_confirmed=include_only_confirmed)

    async def accounts_representatives(self, accounts):
        return await self.rpc.accounts_representatives(accounts)

    async def active_difficulty(self, include_trend=None):
        return await self.rpc.active_difficulty(include_trend=include_trend)

    async def available_supply(self, ):
        return await self.rpc.available_supply()

    async def block(self, hash, json_block=None):
        return await self.rpc.block(hash, json_block=json_block)

    async def block_account(self, hash):
        return await self.rpc.block_account(hash)

    async def block_confirm(self, hash):
        return await self.rpc.block_confirm(hash)

    async def block_count(self, include_cemented=None):
        return await self.rpc.block_count(include_cemented=include_cemented)

    async def block_create(self, type, balance, key, representative, link, previous, work=None, version=None, difficulty=None, json_block=None):
        return await self.rpc.block_create(type, balance, key, representative, link, previous, work=work, version=version, difficulty=difficulty, json_block=json_block)

    async def block_hash(self, block, json_block=None):
        return await self.rpc.block_hash(block, json_block=json_block)

    async def block_info(self, hash, json_block=None):
        return await self.rpc.block_info(hash, json_block=json_block)

    async def blocks(self, hashes, json_block=None):
        return await self.rpc.blocks(hashes, json_block=json_block)

    async def blocks_info(self, hashes, json_block=None, receivable=None, pending=None, source=None, receive_hash=None, include_not_found=None):
        return await self.rpc.blocks_info(hashes, json_block=json_block, receivable=receivable, pending=pending, source=source, receive_hash=receive_hash, include_not_found=include_not_found)

    async def bootstrap(self, address, port, bypass_frontier_confirmation=None, id=None):
        return await self.rpc.bootstrap(address, port, bypass_frontier_confirmation=bypass_frontier_confirmation, id=id)

    async def bootstrap_any(self, force=None, id=None, account=None):
        return await self.rpc.bootstrap_any(force=force, id=id, account=account)

    async def bootstrap_lazy(self, hash, force=None, id=None):
        return await self.rpc.bootstrap_lazy(hash, force=force, id=id)

    async def bootstrap_status(self, ):
        return await self.rpc.bootstrap_status()

    async def chain(self, block, count, offset=None, reverse=None):
        return await self.rpc.chain(block, count, offset=offset, reverse=reverse)

    async def confirmation_active(self, announcements=None):
        return await self.rpc.confirmation_active(announcements=announcements)

    async def confirmation_history(self, hash=None):
        return await self.rpc.confirmation_history(hash=hash)

    async def confirmation_info(self, root, contents=None, json_block=None, representatives=None):
        return await self.rpc.confirmation_info(root, contents=contents, json_block=json_block, representatives=representatives)

    async def confirmation_quorum(self, peer_details=None):
        return await self.rpc.confirmation_quorum(peer_details=peer_details)

    async def database_txn_tracker(self, min_read_time, min_write_time):
        return await self.rpc.database_txn_tracker(min_read_time, min_write_time)

    async def debug_bootstrap_priority_info(self, ):
        return await self.rpc.debug_bootstrap_priority_info()

    async def delegators(self, account, threshold=None, count=None, start=None):
        return await self.rpc.delegators(account, threshold=threshold, count=count, start=start)

    async def delegators_count(self, account):
        return await self.rpc.delegators_count(account)

    async def deterministic_key(self, seed, index):
        return await self.rpc.deterministic_key(seed, index)

    async def election_statistics(self, ):
        return await self.rpc.election_statistics()

    async def epoch_upgrade(self, epoch, key, count=None, threads=None):
        return await self.rpc.epoch_upgrade(epoch, key, count=count, threads=threads)

    async def frontier_count(self, ):
        return await self.rpc.frontier_count()

    async def frontiers(self, account, count=None):
        return await self.rpc.frontiers(account, count=count)

    async def keepalive(self, address, port):
        return await self.rpc.keepalive(address, port)

    async def key_create(self, ):
        return await self.rpc.key_create()

    async def key_expand(self, key):
        return await self.rpc.key_expand(key)

    async def ledger(self, account, count, representative=None, weight=None, receivable=None, pending=None, modified_since=None, sorting=None, threshold=None):
        return await self.rpc.ledger(account, count, representative=representative, weight=weight, receivable=receivable, pending=pending, modified_since=modified_since, sorting=sorting, threshold=threshold)

    async def nano_to_raw(self, amount):
        return await self.rpc.nano_to_raw(amount)

    async def node_id(self, ):
        return await self.rpc.node_id()

    async def node_id_delete(self, ):
        return await self.rpc.node_id_delete()

    async def password_change(self, wallet, password):
        return await self.rpc.password_change(wallet, password)

    async def password_enter(self, wallet, password):
        return await self.rpc.password_enter(wallet, password)

    async def password_valid(self, wallet):
        return await self.rpc.password_valid(wallet)

    async def peers(self, peer_details=None):
        return await self.rpc.peers(peer_details=peer_details)

    async def pending(self, account, count=None, threshold=None, source=None, include_active=None, min_version=None, sorting=None, include_only_confirmed=None):
        return await self.rpc.pending(account, count=count, threshold=threshold, source=source, include_active=include_active, min_version=min_version, sorting=sorting, include_only_confirmed=include_only_confirmed)

    async def pending_exists(self, hash, include_active=None, include_only_confirmed=None):
        return await self.rpc.pending_exists(hash, include_active=include_active, include_only_confirmed=include_only_confirmed)

    async def populate_backlog(self, ):
        return await self.rpc.populate_backlog()

    async def process(self, block, force=None, subtype=None, json_block=None, async_=None):
        return await self.rpc.process(block, force=force, subtype=subtype, json_block=json_block, async_=async_)

    async def pruned_exists(self, hash):
        return await self.rpc.pruned_exists(hash)

    async def raw_to_nano(self, amount):
        return await self.rpc.raw_to_nano(amount)

    async def receivable(self, account, count=None, threshold=None, source=None, include_active=None, min_version=None, sorting=None, include_only_confirmed=None, offset=None):
        return await self.rpc.receivable(account, count=count, threshold=threshold, source=source, include_active=include_active, min_version=min_version, sorting=sorting, include_only_confirmed=include_only_confirmed, offset=offset)

    async def receivable_exists(self, hash, include_active=None, include_only_confirmed=None):
        return await self.rpc.receivable_exists(hash, include_active=include_active, include_only_confirmed=include_only_confirmed)

    async def receive(self, wallet, account, block):
        return await self.rpc.receive(wallet, account, block)

    async def receive_minimum(self, ):
        return await self.rpc.receive_minimum()

    async def receive_minimum_set(self, amount):
        return await self.rpc.receive_minimum_set(amount)

    async def representatives(self, count=None, sorting=None):
        return await self.rpc.representatives(count=count, sorting=sorting)

    async def representatives_online(self, weight=None, accounts=None):
        return await self.rpc.representatives_online(weight=weight, accounts=accounts)

    async def republish(self, hash, sources=None, destinations=None):
        return await self.rpc.republish(hash, sources=sources, destinations=destinations)

    async def search_pending(self, wallet):
        return await self.rpc.search_pending(wallet)

    async def search_pending_all(self, ):
        return await self.rpc.search_pending_all()

    async def search_receivable(self, wallet):
        return await self.rpc.search_receivable(wallet)

    async def search_receivable_all(self, ):
        return await self.rpc.search_receivable_all()

    async def send(self, wallet, source, destination, amount, id=None, work=None):
        return await self.rpc.send(wallet, source, destination, amount, id=id, work=work)

    async def sign_hash(self, hash):
        return await self._sign(hash=hash)

    async def sign_block_with_key(self, block, private_key, json_block=False):
        return await self._sign(key=private_key, block=block, json_block=json_block)

    async def sign_block_with_wallet(self, block, wallet, json_block=False):
        return await self._sign(wallet=wallet, block=block, json_block=json_block)

    async def _sign(self, key=None, wallet=None, block=None, hash=None, json_block=False):
        # Note: This method requires either 'block' or 'hash'. Either 'key' or 'wallet'. Don't use directly.
        return await self.rpc.sign(key=key, wallet=wallet, block=block, hash=hash, json_block=json_block)

    async def stats(self, type):
        return await self.rpc.stats(type)

    async def stats_clear(self, ):
        return await self.rpc.stats_clear()

    async def stop(self, ):
        return await self.rpc.stop()

    async def successors(self, block, count, offset=None, reverse=None):
        return await self.rpc.successors(block, count, offset=offset, reverse=reverse)

    async def telemetry(self, raw=None, address=None, port=None):
        return await self.rpc.telemetry(raw=raw, address=address, port=port)

    async def unchecked(self, count, json_block=None):
        return await self.rpc.unchecked(count, json_block=json_block)

    async def unchecked_clear(self, ):
        return await self.rpc.unchecked_clear()

    async def unchecked_get(self, hash, json_block=None):
        return await self.rpc.unchecked_get(hash, json_block=json_block)

    async def unchecked_keys(self, key, count, json_block=None):
        return await self.rpc.unchecked_keys(key, count, json_block=json_block)

    async def unopened(self, account, count, threshold=None):
        return await self.rpc.unopened(account, count, threshold=threshold)

    async def uptime(self, ):
        return await self.rpc.uptime()

    async def validate_account_number(self, account):
        return await self.rpc.validate_account_number(account)

    async def version(self, ):
        return await self.rpc.version()

    async def wallet_add(self, wallet, key, work=None):
        return await self.rpc.wallet_add(wallet, key, work=work)

    async def wallet_add_watch(self, wallet, accounts):
        return await self.rpc.wallet_add_watch(wallet, accounts)

    async def wallet_balance_total(self, wallet):
        return await self.rpc.wallet_balance_total(wallet)

    async def wallet_balances(self, wallet, threshold=None):
        return await self.rpc.wallet_balances(wallet, threshold=threshold)

    async def wallet_change_seed(self, wallet, seed, count=None):
        return await self.rpc.wallet_change_seed(wallet, seed, count=count)

    async def wallet_contains(self, wallet, account):
        return await self.rpc.wallet_contains(wallet, account)

    async def wallet_create(self, seed=None):
        return await self.rpc.wallet_create(seed=seed)

    async def wallet_destroy(self, wallet):
        return await self.rpc.wallet_destroy(wallet)

    async def wallet_export(self, wallet):
        return await self.rpc.wallet_export(wallet)

    async def wallet_frontiers(self, wallet):
        return await self.rpc.wallet_frontiers(wallet)

    async def wallet_history(self, wallet, modified_since=None):
        return await self.rpc.wallet_history(wallet, modified_since=modified_since)

    async def wallet_info(self, wallet):
        return await self.rpc.wallet_info(wallet)

    async def wallet_key_valid(self, wallet):
        return await self.rpc.wallet_key_valid(wallet)

    async def wallet_ledger(self, wallet, representative=None, weight=None, receivable=None, pending=None):
        return await self.rpc.wallet_ledger(wallet, representative=representative, weight=weight, receivable=receivable, pending=pending)

    async def wallet_lock(self, wallet):
        return await self.rpc.wallet_lock(wallet)

    async def wallet_pending(self, wallet, count=None, threshold=None, source=None):
        return await self.rpc.wallet_pending(wallet, count=count, threshold=threshold, source=source)

    async def wallet_receivable(self, wallet, count=None, threshold=None, source=None):
        return await self.rpc.wallet_receivable(wallet, count=count, threshold=threshold, source=source)

    async def wallet_representative(self, wallet):
        return await self.rpc.wallet_representative(wallet)

    async def wallet_representative_set(self, wallet, representative, work=None):
        return await self.rpc.wallet_representative_set(wallet, representative, work=work)

    async def wallet_republish(self, wallet, count=None):
        return await self.rpc.wallet_republish(wallet, count=count)

    async def wallet_unlock(self, wallet, password):
        return await self.rpc.wallet_unlock(wallet, password)

    async def wallet_work_get(self, wallet):
        return await self.rpc.wallet_work_get(wallet)

    async def work_cancel(self, hash):
        return await self.rpc.work_cancel(hash)

    async def work_generate(self, hash, use_peers=None, difficulty=None, multiplier=None, account=None, version=None, block=None, json_block=None):
        return await self.rpc.work_generate(hash, use_peers=use_peers, difficulty=difficulty, multiplier=multiplier, account=account, version=version, block=block, json_block=json_block)

    async def work_get(self, wallet):
        return await self.rpc.work_get(wallet)

    async def work_peer_add(self, address, port):
        return await self.rpc.work_peer_add(address, port)

    async def work_peers(self, ):
        return await self.rpc.work_peers()

    async def work_peers_clear(self, ):
        return await self.rpc.work_peers_clear()

    async def work_set(self, wallet, account, work):
        return await self.rpc.work_set(wallet, account, work)

    async def work_validate(self, work, hash, difficulty=None, multiplier=None, version=None):
        return await self.rpc.work_validate(work, hash, difficulty=difficulty, multiplier=multiplier, version=version)
