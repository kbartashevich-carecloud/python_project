from functools import reduce, partial

def multiply(a, b):
    return a * b

print(reduce(multiply, [1, 2, 3, 4, 5, 6]))

def greeter(person, greeting):
    return("{}, {}".format(greeting, person))

hier = partial(greeter, greeting='Hi')
print(hier('brother'))