try:
    with open("/file/not/found") as f:
        content = f.read()
except OSError as err:
    print(err.errno, err.strerror)

import os.path

filename = "/file/not/found"
try:
    if not os.path.exists(filename):
        raise ValueError("file doesn't exists", filename)
except ValueError as err:
    message, filename  = err.args[0],  err.args[1]
    print(message, filename)

import traceback

try:
    with open("/file/not/found") as f:
        content = f.read()
except OSError as err:
    trace = traceback.print_exc()
    print(trace)

try:
    raw = input("Enter number: ")
    if not raw.isdigit():
        raise ValueError
except ValueError:
    print("incorrect value")

try:
    raw = input("enter number: ")
    if not raw.isdigit():
        raise ValueError("bad number", raw)
except ValueError as err:
    print("incorrect value!", err)

try:
    raw = input("enter number:")
    if not raw.isdigit():
        raise ValueError("bad number", raw)
except ValueError as err:
    print("incorrect value!", err)
    raise

def get_user_by_id(id):
    assert isinstance(id, int), "id must being int"

    print("doing search")

if __name__ == '__main__':
    get_user_by_id("foo")

%%timeit
my_dict = {"foo": 1}
for _ in range(1000):
    try:
        my_dict["bar"]
    except KeyError:
        pass
