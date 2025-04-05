from event import Event
import requests
from typing import Callable
from utils import get_string
import json


class Client:
    def __init__(self, url: str, callable: Callable):
        self.url = url
        self.callable = callable
        self.closed = True

    def connect(self):
        """
        Connect to Server Sent Events API
        """
        self.closed = False
        stream = requests.get(self.url, stream=True)
        event: Event = Event("", "")
        for line in stream.iter_lines():
            if not line:  # new event
                self.callable(event)
                continue

            inp = get_string(line)
            if inp.startswith("event:"):
                event.name = inp[6:]
            elif inp.startswith("data:"):
                event.data = json.loads(inp[5:])
            if self.closed:
                break
