from functools import wraps
from asyncio import sleep as async_sleep
from time import sleep as sync_sleep
from typing import Optional, Callable, Union, Type


def handle_exceptions(
    exceptions: Union[Type[Exception], tuple[Type[Exception], ...]] = Exception,
    max_retries: int = 3,
    recovery_procedure: Optional[Callable] = None,
    delay: Optional[int] = None,
):
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
