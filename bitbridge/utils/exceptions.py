from rich.console import Console
from rich.traceback import Traceback

console = Console()


class BaseBitBridgeException(Exception):
    """Base exception for BitBridge."""

    def __init__(self, message: str):
        self.message = message
        super().__init__(self.message)

    def display(self):
        """Display the error using Rich's console."""
        console.print(Traceback())
        console.print(self.message, style="bold red")


class ConfigurationError(BaseBitBridgeException):
    """Raised when there is an issue with the configuration."""

    pass


class BlockchainRPCError(BaseBitBridgeException):
    """Exception raised for errors in the Blockchain RPC group."""

    pass


class ControlRPCError(BaseBitBridgeException):
    """Exception raised for errors in the Control RPC group."""

    pass


class NetworkRPCError(BaseBitBridgeException):
    """Exception raised for errors in the Network RPC group."""

    pass


class RawTransactionsRPCError(BaseBitBridgeException):
    """Exception raised for errors in the Raw Transactions RPC group."""

    pass


class UtilRPCError(BaseBitBridgeException):
    """Exception raised for errors in the Util RPC group."""


class WalletRPCError(BaseBitBridgeException):
    """Exception raised for errors in the Wallet RPC group."""

    pass
