import pytest
from bitbridge.rpc.config import BitBridgeConfig


@pytest.fixture
def bridge_facade_config():
    return {
        "url": "http://localhost:18443",
        "username": "user",
        "password": "password",
    }


@pytest.fixture
def bridge_config(bridge_facade_config):
    return BitBridgeConfig(**bridge_facade_config)


def test_console_exception():
    from bitbridge.utils.exceptions import BaseBitBridgeException

    try:
        raise BaseBitBridgeException("This is a test error message.")
    except BaseBitBridgeException as e:
        e.display()
