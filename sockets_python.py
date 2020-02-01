import socket
import threading
import multiprocessing

with socket.socket() as sock:
    sock.bind(("", 10001))
    sock.listen()

    workers_count = 3
    workers_list = [multiprocessing.Process(target=worker, args=(sock,))
                    for _ in range(workers_count)]

    for w in workers_list:
        w.start()

    for w in workers_list:
        w.join()

def worker(sock):
    while True:
        conn, addr = sock.accept()
        print("pid", os.getpid())
        th = threading.Thread(target=process-request, args=(conn, addr))
        th.start()


def process_request(conn, addr):
    print("connected client:", addr)
    with conn:
        while True:
            data = conn.recv(1024)
            if not data:
                break
            print(data.decode("utf8"))

import socket
import select


sock = socket.socket()
sock.bind(("", 10001))
sock.listen()

conn1, addr = sock.accept()
conn2, addr = sock.accept()

conn1.setblocking(0)
conn2.setblocking(0)

epoll = select.epoll()
epoll.register(conn1.fileno(), select.EPOLLIN | select.EPOLLOUT)
epoll.register(conn2.fileno(), select.EPOLLIN | select.EPOLLOUT)

conn_map = {
    conn1.fileno(): conn1,
    conn2.fileno(): conn2
}
