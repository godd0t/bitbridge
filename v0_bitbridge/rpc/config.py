from typing import Callable


class BitBridgeConfig:
    def __init__(
        self,
        url: str,
        username: str,
        password: str,
        retries: int = 1,
        timeout: int = 3,
    ):
        self.url = url
        self.username = username
        self.password = password
        self.retries = retries
        self.timeout = timeout
