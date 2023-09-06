from functools import wraps
from asyncio import sleep as async_sleep
from time import sleep as sync_sleep
from typing import Optional, Callable, Union, Type

from bitbridge.rpc.config import BitBridgeConfig
from bitbridge.utils.exceptions import ConfigurationError


def handle_exceptions(
    exceptions: Union[Type[Exception], tuple[Type[Exception], ...]] = Exception,
    max_retries: int = None,
    recovery_procedure: Optional[Callable] = None,
    delay: Optional[int] = None,
):
    max_retries = max_retries or BitBridgeConfig.default_max_retries
    recovery_procedure = (
        recovery_procedure or BitBridgeConfig.default_recovery_procedure
    )
    delay = delay or BitBridgeConfig.default_delay

    def decorator(func):
        @wraps(func)
        def wrapper(instance, *args, **kwargs):
            for i in range(max_retries):
                try:
                    return func(instance, *args, **kwargs)
                except exceptions as e:
                    if i == max_retries - 1:
                        raise e
                    if recovery_procedure:
                        recovery_procedure(instance, *args, **kwargs)
                    if delay:
                        sync_sleep(delay)
                    continue

        return wrapper

    return decorator


def async_handle_exceptions(
    exceptions: Union[Type[Exception], tuple[Type[Exception], ...]] = Exception,
    max_retries: int = 3,
    recovery_procedure: Optional[Callable] = None,
    delay: Optional[int] = None,
):
    max_retries = max_retries or BitBridgeConfig.default_max_retries
    recovery_procedure = (
        recovery_procedure or BitBridgeConfig.default_recovery_procedure
    )
    delay = delay or BitBridgeConfig.default_delay

    def decorator(func):
        @wraps(func)
        async def wrapper(instance, *args, **kwargs):
            for i in range(max_retries):
                try:
                    return await func(instance, *args, **kwargs)
                except exceptions as e:
                    if i == max_retries - 1:
                        raise e
                    if recovery_procedure:
                        await recovery_procedure(instance, *args, **kwargs)
                    if delay:
                        await async_sleep(delay)
                    continue

        return wrapper

    return decorator


def config_validator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        config_instance = BitBridgeConfig._instance  # noqa
        if config_instance is None or not hasattr(config_instance, "is_initialized"):
            raise ConfigurationError("BitBridgeConfig has not been initialized.")
        return func(*args, **kwargs)

    return wrapper
