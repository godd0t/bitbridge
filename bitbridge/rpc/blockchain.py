from bitbridge.rpc_delegate import RpcDelegate
from bitbridge.utils.constants import (
    GET_BEST_BLOCK_HASH,
    GET_BLOCK,
    GET_BLOCKCHAIN_INFO,
)


class BaseBlockchain:
    def __init__(self, rpc_delegate: RpcDelegate):
        self.rpc_delegate = rpc_delegate


class BlockchainSync(BaseBlockchain):
    def get_best_block_hash(self):
        return self.rpc_delegate.send_request(GET_BEST_BLOCK_HASH)

    def get_block(self, blockhash: str, verbosity: int = 1):
        return self.rpc_delegate.send_request(GET_BLOCK, [blockhash, verbosity])

    def get_blockchain_info(self):
        return self.rpc_delegate.send_request(GET_BLOCKCHAIN_INFO)


class BlockchainAsync(BaseBlockchain):
    async def get_best_block_hash(self):
        return await self.rpc_delegate.send_request_async(GET_BEST_BLOCK_HASH)

    async def get_block(self, blockhash: str, verbosity: int = 1):
        return await self.rpc_delegate.send_request_async(
            GET_BLOCK, [blockhash, verbosity]
        )

    async def get_blockchain_info(self):
        return await self.rpc_delegate.send_request_async(GET_BLOCKCHAIN_INFO)
