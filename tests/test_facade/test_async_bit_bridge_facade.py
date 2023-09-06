from bitbridge import AsyncBitBridgeFacade


async def test_bridge_facade(bridge_config):
    bridge = AsyncBitBridgeFacade(bridge_config)
    best_block_hash = await bridge.blockchain.get_best_block_hash()
    print(best_block_hash)
