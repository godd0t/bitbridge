from bitbridge.rpc.base_rpc import BaseRPC
from bitbridge.utils.constants import (
    ABANDON_TRANSACTION,
    ABORT_RESCAN,
    ADD_MULTISIG_ADDRESS,
)


class BaseWallet(BaseRPC):
    pass


class WalletSync(BaseWallet):
    def abandon_transaction(self, txid: str):
        return self.rpc_delegate.send_request(ABANDON_TRANSACTION, [txid])

    def abort_rescan(self):
        return self.rpc_delegate.send_request(ABORT_RESCAN)

    def add_multisig_address(self, nrequired: int, keys: list, label: str = None):
        return self.rpc_delegate.send_request(
            ADD_MULTISIG_ADDRESS, [nrequired, keys, label]
        )


class WalletAsync(BaseWallet):
    async def abandon_transaction(self, txid: str):
        return await self.rpc_delegate.send_request_async(ABANDON_TRANSACTION, [txid])

    async def abort_rescan(self):
        return await self.rpc_delegate.send_request_async(ABORT_RESCAN)

    async def add_multisig_address(self, nrequired: int, keys: list, label: str = None):
        return await self.rpc_delegate.send_request_async(
            ADD_MULTISIG_ADDRESS, [nrequired, keys, label]
        )
