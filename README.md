# py-sse-client

A simple server sent events client for python

## Installation

```bash
pip3 install py-sse-client
```

## Usage

```python
import pysse

def listener(event):
    print(event)

client = pysse.Client("https://example.com/sse", listener)
client.connect()
```
