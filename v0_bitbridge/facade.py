from bitbridge.rpc.base import BitBridgeBaseRPC
from bitbridge.rpc._sync.blockchain import BlockchainSync
from bitbridge.rpc._sync.wallet import WalletSync
from bitbridge.rpc.config import BitBridgeConfig


class BitBridgeFacade(BitBridgeBaseRPC):
    def __init__(self, config: BitBridgeConfig):
        super().__init__(config)
        self.blockchain = BlockchainSync(config)
        self.wallet = WalletSync(config)
