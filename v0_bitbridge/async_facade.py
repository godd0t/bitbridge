from bitbridge.rpc.base import BitBridgeBaseRPC
from bitbridge.rpc._async.blockchain import BlockchainAsync
from bitbridge.rpc._async.wallet import WalletAsync
from bitbridge.rpc.config import BitBridgeConfig


class AsyncBitBridgeFacade(BitBridgeBaseRPC):
    def __init__(self, config: BitBridgeConfig):
        super().__init__(config)
        self.blockchain = BlockchainAsync(config)
        self.wallet = WalletAsync(config)
