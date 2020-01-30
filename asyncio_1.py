import asyncio_1


async def hello_world():
    while True:
        print("Hello World!")
        await asyncio_1.sleep(1.0)

loop = asyncio_1.get_event_loop()
loop.run_until_complete(hello_world())
loop.close()