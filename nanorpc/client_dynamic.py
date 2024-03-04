from asyncio import TimeoutError, sleep as aio_sleep
from .versions.handler import NodeVersion, get_commands_for_version
from aiohttp import ClientSession, ClientConnectorError, BasicAuth


def __convert_value(value):
    """Converts a value to its appropriate string representation."""
    if isinstance(value, bool):
        return str(value).lower()
    elif isinstance(value, int):
        return str(value)
    else:
        return value


def __strip_trailing_underscore(arg):
    """Removes trailing underscore from a string if it exists."""
    # For example 'async' is reserved in Python but also used as parameter in the rpc calls.
    # We pass 'async_' in the python method and convert it back to 'async' for teh rpc call
    return arg[:-1] if arg.endswith('_') else arg


def generate_method(command, required, optional):
    async def method(self, *args, **kwargs):
        payload = {"action": command}
        for arg, value in zip(required, args):
            payload[arg] = __convert_value(value)
        for arg in optional:
            # Handle arguments that may end with an underscore
            payload_arg = __strip_trailing_underscore(arg)
            if arg in kwargs and kwargs[arg] is not None:
                payload[payload_arg] = __convert_value(kwargs[arg])
        return await self.process_payloads([payload])

    # Set the name and the docstring of the new function
    method.__name__ = command
    method.__doc__ = f"Execute the {command} command."

    return method


class MaxRetriesExceededError(Exception):
    """Raised when all retries are exhausted"""
    pass


class NanoRpc:
    RETRY_ON_EXCEPTIONS = (ClientConnectorError, TimeoutError,
                           ConnectionResetError)

    def __init__(self,
                 url,
                 node_version: NodeVersion,
                 max_retries=3,
                 username=None,
                 password=None,
                 auth_key=None,
                 app_name=None,
                 app_email=None,
                 wrap_json=False):
        self.url = url
        self.username = username
        self.password = password
        self.max_retries = max_retries
        self.wrap_json = wrap_json
        self.auth = BasicAuth(username,
                              password) if username and password else None
        self.headers = self._set_headers(auth_key, app_name, app_email)
        self.session = None
        self.commands = get_commands_for_version(node_version)
        self._generate_methods()

    def _set_headers(self, auth_key, app_name, app_email):
        headers = {"Authorization": f"Bearer {auth_key}"} if auth_key else {}
        if app_name:
            headers["nano-app"] = app_name
        if app_email:
            headers["nano-app-admin"] = app_email
        return headers

    def _generate_methods(self):
        for command, params in self.commands.items():
            method = generate_method(command, params["required"],
                                     params["optional"])
            bound_method = method.__get__(
                self, NanoRpc)  # This binds the method to the instance
            setattr(self, method.__name__, bound_method)

    async def _retry_on_exception(self, coroutine, *args, retries):
        for retry in range(retries):
            try:
                return await coroutine(*args)
            except self.RETRY_ON_EXCEPTIONS as e:
                if retry == retries - 1:  # If this was the last retry
                    raise MaxRetriesExceededError(
                        f"All {self.max_retries - retry} retries exhausted for {coroutine.__name__}. Last error: {str(e)}"
                    ) from None
                await aio_sleep(0.5 * 2**retry)

    async def _request_with_retry(self, coroutine, *args, **kwargs):
        return await self._retry_on_exception(coroutine,
                                              *args,
                                              retries=self.max_retries,
                                              **kwargs)

    async def _request(self, payloads):
        async with ClientSession(auth=self.auth) as session:
            async with session.post(self.url, json=payloads[0], headers=self.headers) as response:
                response_data = await response.json()
                if self.wrap_json and not isinstance(response_data, dict):
                    # Wrap the response data in a JSON structure
                    response_data = {
                        "msg": response_data,
                        "error": "wrapped into valid json"
                    }
                return response_data

    async def process_payloads(self, payloads):
        return await self._request_with_retry(self._request, payloads)
