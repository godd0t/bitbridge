from typing import Optional, Callable

from bitbridge.utils.helpers import BaseSingleton


class BitBridgeConfig(BaseSingleton):
    default_max_retries: int = 3
    default_recovery_procedure: Optional[Callable] = None
    default_delay: Optional[int] = 1

    def __init__(
        self,
        url: str,
        username: str,
        password: str,
        retries: int | None = None,
        timeout: int | None = None,
        logging_level: str = "INFO",
    ):
        if not hasattr(self, "is_initialized"):
            self.url = url
            self.username = username
            self.password = password
            self.retries = retries
            self.timeout = timeout
            self.logging_level = logging_level
            self.is_initialized = True
