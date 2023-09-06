import httpx

from bitbridge.rpc.config import BitBridgeConfig
from bitbridge.utils.decorators import handle_exceptions, async_handle_exceptions
from bitbridge.utils.enums import Mode


class RpcDelegate:
    def __init__(self, config: BitBridgeConfig, mode: Mode = Mode.SYNC):
        self.config = config
        self._initial_params = {"jsonrpc": "2.0"}
        self._http_client = httpx.Client if mode == Mode.SYNC else httpx.AsyncClient

    def _get_auth(self):
        return httpx.BasicAuth(self.config.username, self.config.password)

    def _construct_payload(self, method: str, params: list | None = None):
        if params is None:
            params = []
        return {**self._initial_params, "method": method, "params": params}

    @handle_exceptions(httpx.HTTPError)
    def send_request(self, method: str, params: list | None = None):
        payload = self._construct_payload(method, params)
        response = self._http_client().post(
            self.config.url, json=payload, auth=self._get_auth()
        )
        response.raise_for_status()
        return response.json()

    @async_handle_exceptions(httpx.HTTPError)
    async def send_request_async(self, method: str, params: list | None = None):
        payload = self._construct_payload(method, params)
        async with self._http_client() as client:
            response = await client.post(
                self.config.url, json=payload, auth=self._get_auth()
            )
            response.raise_for_status()
            return response.json()
