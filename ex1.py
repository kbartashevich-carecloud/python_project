import time
import os

# foo = "bar"
#
# if os.fork() == 0:
#     foo = "baz"
#     print("child:", foo)
# else:
#     print("parent:", foo)
#     os.wait()

# f = open("data.txt")
# foo = f.readline()
#
# if os.fork() == 0:
#     foo = f.readline()
#     print("child:", foo)
# else:
#     foo = f.readline()
#     print("parent:", foo)

# from multiprocessing import Process
#
# def f(name):
#     print("hello", name)
#
#
# p = Process(target=f, args=("Bob",))
# p.start()
# p.join()

# from multiprocessing import Process
#
#
# class PrintProcess(Process):
#     def __init__(self, name):
#         super().__init__()
#         self.name = name
#
#     def run(self):
#         print("hello", self.name)
#
# p = PrintProcess("Mike")
# p.start()
# p.join()

from threading import Thread
#
# def f(name):
#     print("hello", name)
#
# th = Thread(target=f, args=("Bob",))
# th.start()
# th.join()

# from threading import Thread
#
# class PrintThread(Thread):
#     def __init__(self, name):
#         super().__init__()
#         self.name = name
#
#     def run(self):
#         print("hello", self.name)
#
#
# th = PrintThread("Mike")
# th.start()
# th.join()


# from concurrent.futures import ThreadPoolExecutor, as_completed
#
# def f(a):
#     return a * a
#
# with ThreadPoolExecutor(max_workers=3) as pool:
#     results = [pool.submit(f, i) for i in range(10)]
#
#     for future in as_completed(results):
#         print(future.result())

# from queue import Queue
# from threading import Thread
#
# def worker(q, n):
#     while True:
#         item = q.get()
#         if item is None:
#             break
#         print("process data:", n, item)
#
#
# q = Queue(5)
# th1 = Thread(target=worker, args=(q, 1))
# th2 = Thread(target=worker, args=(q, 2))
# th1.start(); th2.start()
#
# for i in range(50):
#     q.put(i)
#
# q.put(None); q.put(None)
# th1.join(); th2.join()

# import threading
#
# class Point(object):
#     def __init__(self, x, y):
#         self.mutex = threading.RLock()
#         self.set(x, y)
#
#     def get(self):
#         with self.mutex:
#             return (self.x, self.y)
#
#     def set(self, x, y):
#         with self.mutex:
#             self.x = x
#             self.y = y
#
# my_point = Point(10, 20)
# my_point.set(15, 10)
# print(my_point.get())

import threading
#
# a = threading.RLock()
# b = threading.RLock()
#
# def foo():
#     try:
#         a.acquire()
#         b.acquire()
#     finally:
#         a.release()
#         b.release()

# class Queue(object):
#     def __init__(self, size=5):
#         self._size = size
#         self._queue = []
#         self._mutex = threading.RLock()
#         self._empty = threading.Condition(self._mutex)
#         self._full = threading.Condition(self._mutex)
#
#     def put(self, val):
#         with self._full:
#             while len(self._queue) >= self._size:
#                 self._full.wait()
#             self._queue.append(val)
#             self._empty.notify()
#
#     def get(self):
#         with self._empty:
#             while len(self._queue) == 0:
#                 self._empty.wait()
#             ret = self._queue.pop(0)
#             self._full.notify()
#             return ret

# import time
# import os
#
# pid = os.fork()
#
# if pid == 0:
#     print("Child process: ", os.getpid())
#     time.sleep(2)
# else:
#     print("Parent process: ", os.getpid())
#     os.wait()

from threading import Thread
import time

def count(n):
    while n > 0:
        n -= 1

t0 = time.time()
count(100_000_000)
count(100_000_000)
print(time.time() - t0)

#parallel run
t0 = time.time()
th1 = Thread(target=count, args=(100_000_000,))
th2 = Thread(target=count, args=(100_000_000,))

th1.start(); th2.start()
th1.join(); th2.join()
print(time.time() - t0)
