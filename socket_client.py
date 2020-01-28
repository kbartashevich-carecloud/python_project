import socket
#
# sock = socket.socket()
# sock.connect(("127.0.0.1", 10001))
# sock.sendall("ping".encode("utf8"))
# sock.close()
#

with socket.create_connection(("127.0.0.1", 10001)) as sock:
    sock.settimeout(2)
    try:
        sock.sendall("ping".encode("utf8"))
    except socket.timeout:
        print("send data timeout")
    except socket.error as ex:
        print("send data error:", ex)
    sock.close()
