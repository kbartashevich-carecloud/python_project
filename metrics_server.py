import asyncio

storage = dict({})
req_types = {"get", "put"}


def process_data(data):
    if not data or "\n" not in data:
        return "error\nwrong command\n\n"

    parsed_req = data.strip("\n").split(" ")
    if len(parsed_req) != 4 and len(parsed_req) != 2:
        return "error\nwrong command\n\n"

    if parsed_req[0] not in req_types:
        return "error\nwrong command\n\n"

    if parsed_req[0] == "get":

        key = parsed_req[1]

        if key == "*":
            response_t = "ok"

            for metric in storage:
                values = storage[metric]
                response_raw = [f"\n{metric} {val} {ts}" for val, ts in values]
                response_raw = "".join(response_raw)
                response_t = response_t + response_raw

            response_t = response_t + "\n\n"
            return response_t

        if key not in storage:
            return "ok\n\n"

        values = storage[key]
        response = [f"\n{key} {val} {ts}" for val, ts in values]
        response = "".join(response)
        response = f"ok{response}\n\n"

        return response

    else:
        tp, key, val, timestamp = parsed_req


        # if "." not in key:
        #     return "ok\n\n"

        try:
            timestamp = int(timestamp)
            val = float(val)
            ex_storage = storage.setdefault(key, [])
            if (val, timestamp) not in ex_storage:
                ex_storage.append((val, timestamp))
            return "ok\n\n"
        except Exception as ex:
            return "error\nwrong command\n\n"




class ClientServerProtocol(asyncio.Protocol):
    def connection_made(self, transport):
        self.transport = transport

    def data_received(self, data):
        resp = data.decode()
        response = process_data(resp)

        self.transport.write(response.encode())


def run_server(host, port):
    loop = asyncio.get_event_loop()
    coro = loop.create_server(
        ClientServerProtocol,
        host, port
    )
    server = loop.run_until_complete(coro)
    try:
        loop.run_forever()
    except KeyboardInterrupt:
        pass
    server.close()
    loop.run_until_complete(server.wait_closed())
    loop.close()