from bitbridge import AsyncBitBridgeFacade


async def test_async_abandon_transaction(bridge_facade_config):
    facade_ = AsyncBitBridgeFacade(**bridge_facade_config)
    txid = "0d36fae3b5a89547fa1fa29a678261c8a1690818927dbb996cf47d5b1737550a"
    result = await facade_.wallet.abandon_transaction(txid)
    print(result)


async def test_async_abort_rescan(bridge_facade_config):
    facade_ = AsyncBitBridgeFacade(**bridge_facade_config)
    result = await facade_.wallet.abort_rescan()
    print(result)


async def test_async_add_multisig_address(bridge_facade_config):
    facade_ = AsyncBitBridgeFacade(**bridge_facade_config)
    nrequired = 2
    keys = [
        "bcrt1qzq5s3e00258l6fhntr22c4d4mnjnnpa73za73a",
        "bcrt1qjj0lmfj5tulknjegjm3e70skpuwzp573s8lfhz",
    ]
    address_type = "legacy"
    result = await facade_.wallet.add_multisig_address(
        nrequired=nrequired, keys=keys, address_type=address_type
    )
    print(result)
