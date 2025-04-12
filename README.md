# py-sse-client

A simple asynchronous Server Sent Events (SSE) client for Python.

For more information about Server Sent Events, refer to [MDN Web Docs](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events).

## Installation

Install the package using pip:

```bash
pip install py-sse-client
```

## Usage

#### Quickstart

```python
import asyncio
import pysse

def listener(event):
    print(event)

async def main():
    client = pysse.Client("https://example.com/sse", listener)
    await client.connect()

if __name__ == "__main__":
    asyncio.run(main())
```

#### Creating a Client

To create a client, use the `Client` class. The constructor accepts the following arguments:

- `url`:
  - The URL of the SSE endpoint
  - Type: `str`
  - Required
- `callable`:
  - A callback function that will be invoked whenever an event is received
  - The callback receives an `Event` object as its argument
  - Type: `Callable`
  - Required
- `param`:
  - Query parameters to include in the request
  - Default is an empty dictionary
  - Type: `dict`
  - Optional
- `headers`:
  - HTTP headers to include in the request
  - Default is an empty dictionary
  - Type: `dict`
  - Optional

_Example:_

```python
from pysse import Client

def listener(event):
    print(f"Event Name: {event.name}")
    print(f"Event Data: {event.data}")

client = Client(
    url="https://example.com/sse",
    callable=listener,
    param={"token": "your_token"},
    headers={"Authorization": "Bearer your_token"}
)
```

#### Connecting to a Server Sent Events API

To connect to the SSE API, call the `connect` method of the `Client` instance. This method is asynchronous and should be awaited.

_Example:_

```python
import asyncio

async def main():
    await client.connect()

asyncio.run(main())
```

#### Disconnecting from the Server Sent Events API

To disconnect from the SSE API, call the `close` method of the `Client` instance. This method is also asynchronous and should be awaited.

_Example:_

```python
async def main():
    await client.close()

asyncio.run(main())
```

## API Reference

#### `class pysse.Client`

**Constructor**

```python
Client(url: str, callable: Callable, param: dict = {}, headers: dict = {})
```

**Arguments**:
- `url` (str): The URL of the SSE endpoint
- `callable` (Callable): A callback function to handle incoming events
- `param` (dict, optional): Query parameters for the request
- `headers` (dict, optional): HTTP headers for the request

**Methods**

- `async connect() -> None`  
  Connects to the SSE API and starts listening for events

- `async close() -> None`  
  Disconnects from the SSE API

- `is_closed() -> bool`  
  Returns `True` if the connection is closed, otherwise `False`

#### `class pysse.Event`

A data class representing an SSE event

**Attributes**:
- `name` (str): The name of the event
- `data` (dict): The data associated with the event

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Links

- [Homepage](https://github.com/dilanka-rathnasiri/py-sse-client)
- [Documentation](https://github.com/dilanka-rathnasiri/py-sse-client)
- [Source Code](https://github.com/dilanka-rathnasiri/py-sse-client)
