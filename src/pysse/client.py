from .event import Event
from typing import Callable
import json
import aiohttp
import asyncio
from .exceptions import HttpRespException


class Client:
    def __init__(self, url: str, callable: Callable, param={}, headers={}):
        self.url: str = url
        self.param: dict = param
        self.headers: dict = headers
        self.callable: Callable = callable
        self.__task: asyncio.Task = None
        self.__closed = True

    async def connect(self):
        """
        Asynchronously connect to Server Sent Events API
        """
        self.closed = False
        async with aiohttp.ClientSession() as session:
            async with session.get(
                self.url, params=self.param, headers=self.headers
            ) as response:
                if response.status != 200:
                    raise HttpRespException(
                        message="Connection failed",
                        status=response.status,
                        headers=response.headers,
                    )
                self.__task = asyncio.create_task(self.__read_stream(response.content))
                try:
                    await self.__task
                except asyncio.CancelledError:
                    pass

    async def __read_stream(self, stream: aiohttp.StreamReader) -> None:
        """
        Read from HTTP stream
        """
        event: Event = Event("", "")
        async for line in stream:
            inp = line.decode("utf-8")
            if inp == "\n":  # new event
                self.callable(event)
                continue

            if inp.startswith("event:"):
                event.name = inp[6:-1]
            elif inp.startswith("data:"):
                event.data = json.loads(inp[5:])

    async def close(self):
        """
        Close the connection of server sent event stream
        """
        if not (self.__closed) and self.__task is not None:
            self.__task.cancel()
            self.__closed = True

    def is_closed(self):
        return self.__closed
