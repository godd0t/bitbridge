import httpx

from bitbridge.rpc.config import BitBridgeConfig
from bitbridge.utils.decorators import handle_errors, async_handle_errors


class BitBridgeBaseRPC:
    def __init__(self, config: BitBridgeConfig):
        self._initial_params = {"jsonrpc": "2.0"}
        self.config = config

    def _get_auth(self):
        return httpx.BasicAuth(self.config.username, self.config.password)

    def _get_payload(self, method: str, params: list | None = None):
        if params is None:
            params = []
        return {**self._initial_params, "method": method, "params": params}

    @handle_errors(httpx.HTTPError)
    def send_request(self, method: str, params: list | None = None):
        payload = self._get_payload(method, params)
        response = httpx.post(self.config.url, json=payload, auth=self._get_auth())
        response.raise_for_status()
        return response.json()

    @async_handle_errors(httpx.HTTPError)
    async def send_request_async(self, method: str, params: list | None = None):
        payload = self._get_payload(method, params)
        async with httpx.Client() as client:
            response = await client.post(
                self.config.url, json=payload, auth=self._get_auth()
            )
            response.raise_for_status()
            return response.json()
