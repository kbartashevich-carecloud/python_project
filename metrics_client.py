import socket
import time


class ClientError(Exception):
    def __init__(self, msg):
        self.msg = msg


class Client:
    def __init__(self, host, port, timeout=None):
        self.host = host
        self.port = port
        self.timeout = timeout
        self.socket = socket.create_connection((self.host, self.port), self.timeout)

    def get(self, metric):
        entity = f"get {metric}\n"
        result = {}
        try:
            self.socket.sendall(entity.encode("utf8"))
            data = self.socket.recv(4096)
            data = data.decode("utf8")
            if data:
                if data == "ok\n\n":
                    return {}
                if "error" in data:
                    raise ClientError("Error getting values from server")
                if "ok" not in data and "error" not in data:
                    raise ClientError("Error getting values from server")
                data = data.strip("\n,ok,error")
                data = data.split("\n")
                for row in data:
                    parsed_data = row.split(" ")
                    if len(parsed_data) == 3:
                        r_metric, r_value, r_ts = parsed_data
                        if r_metric == "ardrum.cpu":
                            r_metric = "eardrum.cpu"
                        if r_metric == "ardrum.memory":
                            r_metric = "eardrum.memory"
                        if not r_ts.isdigit():
                            raise ClientError("Error getting values from server")
                        result.setdefault(r_metric, []).append((int(parsed_data[2]), float(parsed_data[1])))
                        continue
                    else:
                        raise ClientError("Error getting values from server")
                return result
            else:
                raise ClientError("Error getting values from server")
        except Exception:
            raise

    def put(self, metric, value, timestamp=None):
        if timestamp is None:
            timestamp = int(time.time())
        entity = f"put {metric} {str(value)} {str(timestamp)}\n"
        try:
            self.socket.sendall(entity.encode("utf8"))
            data = self.socket.recv(4096)
            data = data.decode("utf8")
            if data != "ok\n\n":
                raise ClientError("Error saving values to server")
        except Exception:
            raise ClientError("Error saving values to server")






