while True:
    try:
        raw = input("Enter number: ")
        number = int(raw)
        break
    except ValueError:
        print("incorrect value")
    except KeyboardInterrupt:
        print("exit")
        break

total_count = 100_000
while True:
    try:
        raw = input("enter number: ")
        number = int(raw)
        total_count = total_count / number
        break
    except (ValueError, ZeroDivisionError):
        print("incorrect value!")

database = {
    "red": ["fox", "flower"],
    "green": ["peace", "M", "python"]
}

try:
    color = input("enter color: ")
    number = input("enter number in order: ")

    label = database[color][int(number)]
    print("you chose:", label)
except LookupError:
    print("Object didn't found")


f = open("/etc/hosts")
try:
    for line in f:
        print(line.rstrip("\n"))
        1 / 0
except OSError:
    print("error")
finally:
    f.close()