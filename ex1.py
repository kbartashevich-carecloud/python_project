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

f = open("data.txt")
foo = f.readline()

if os.fork() == 0:
    foo = f.readline()
    print("child:", foo)
else:
    foo = f.readline()
    print("parent:", foo)
