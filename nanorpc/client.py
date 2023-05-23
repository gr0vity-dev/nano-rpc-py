from asyncio import TimeoutError, sleep as aio_sleep
from .versions.handler import NodeVersion, COMMANDS_BASE, COMMANDS_CHANGES
from aiohttp import ClientSession, TCPConnector, ClientConnectorError, BasicAuth


def generate_method(command, required, optional):

    async def method(self, *args, **kwargs):
        payload = {"action": command}
        for arg, value in zip(required, args):
            payload[arg] = value
        for arg in optional:
            if arg in kwargs:
                payload[arg] = kwargs[arg]
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
                 password=None):
        self.url = url
        self.username = username
        self.password = password
        self.max_retries = max_retries
        self.auth = BasicAuth(username,
                              password) if username and password else None
        self.session = None
        self.commands = self._set_commands(node_version)
        self._generate_methods()

    def _set_commands(self, selected_version):
        commands = COMMANDS_BASE.copy()
        for version in sorted(NodeVersion):
            if version <= selected_version:
                commands.update(COMMANDS_CHANGES[version])  # Apply changes
        return commands

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
            async with session.post(self.url, json=payloads[0]) as response:
                return await response.json()

    async def process_payloads(self, payloads):
        return await self._request_with_retry(self._request, payloads)