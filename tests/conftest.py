import pytest
from os import getenv
from bitbridge.rpc.config import BitBridgeConfig


@pytest.fixture
def bridge_facade_config():
    user = getenv("RPC_USER", "user")
    password = getenv("RPC_PASS", "password")
    return {
        "url": "http://localhost:18443",
        "username": user,
        "password": password,
    }


@pytest.fixture
def bridge_config(bridge_facade_config):
    return BitBridgeConfig(**bridge_facade_config)
