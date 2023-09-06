import httpx

from bitbridge.rpc.blockchain import BlockchainSync, BlockchainAsync
from bitbridge.rpc.config import BitBridgeConfig
from bitbridge.utils.decorators import async_handle_exceptions, handle_exceptions


class BaseBitBridgeFacade:
    def __init__(self, config: BitBridgeConfig):
        self.config = config
        self._initial_params = {"jsonrpc": "2.0"}

    def _get_auth(self):
        return httpx.BasicAuth(self.config.username, self.config.password)

    def _get_payload(self, method: str, params: list | None = None):
        if params is None:
            params = []
        return {**self._initial_params, "method": method, "params": params}


class BitBridgeFacade(BaseBitBridgeFacade):
    def __init__(self, config: BitBridgeConfig):
        super().__init__(config)
        self.blockchain = BlockchainSync(self)

    @handle_exceptions(httpx.HTTPError)
    def send_request(self, method: str, params: list | None = None):
        payload = self._get_payload(method, params)
        response = httpx.post(self.config.url, json=payload, auth=self._get_auth())
        response.raise_for_status()
        return response.json()


class AsyncBitBridgeFacade(BaseBitBridgeFacade):
    def __init__(self, config: BitBridgeConfig):
        super().__init__(config)
        self.blockchain = BlockchainAsync(self)

    @async_handle_exceptions(httpx.HTTPError)
    async def send_request_async(self, method: str, params: list | None = None):
        payload = self._get_payload(method, params)
        async with httpx.Client() as client:
            response = await client.post(
                self.config.url, json=payload, auth=self._get_auth()
            )
            response.raise_for_status()
            return response.json()
