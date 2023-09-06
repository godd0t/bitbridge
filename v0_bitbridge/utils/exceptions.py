from rich.console import Console
from rich.traceback import Traceback

console = Console()


class BitBridgeError(Exception):
    """Base exception for BitBridge."""

    def __init__(self, message):
        super().__init__(message)
        console.print(message, style="bold red")


class BlockchainRPCError(BitBridgeError):
    """Exception raised for errors in the Blockchain RPC group."""

    pass


class ControlRPCError(BitBridgeError):
    """Exception raised for errors in the Control RPC group."""

    pass


class NetworkRPCError(BitBridgeError):
    """Exception raised for errors in the Network RPC group."""

    pass


class RawTransactionsRPCError(BitBridgeError):
    """Exception raised for errors in the Raw Transactions RPC group."""

    pass


class UtilRPCError(BitBridgeError):
    """Exception raised for errors in the Util RPC group."""


class WalletRPCError(BitBridgeError):
    """Exception raised for errors in the Wallet RPC group."""

    pass
