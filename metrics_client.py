import asyncio
import time


class ClientError(Exception):
    def __init__(self, prev, nex, msg):
        self.prev = prev
        self.next = nex
        self.msg = msg


class Client:
    def __init__(self, host, port, timeout=None):
        self.host = host
        self.port = port
        self.timeout = timeout
        self.loop = asyncio.get_event_loop()
        self.reader = None
        self.writer = None

    async def create_tcp_client(self):
        reader, writer = await asyncio.open_connection(self.host, self.port, self.loop)
        self.reader = reader
        self.writer = writer

    def stop_server(self):
        self.loop.close()

    async def get(self, metric):
        pass

    async def put(self, metric, value, timestamp=None):
        if timestamp is None:
            timestamp = int(time.time())
        try:
            pass
        except:
            raise ClientError