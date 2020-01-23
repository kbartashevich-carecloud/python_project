def even_range(start, end):
    current = start
    while current < end:
        yield current
        current += 2


# def list_generator(list_obj):
#     for item in list_obj:
#         yield item
#         print('After yielding {}'.format(item))
#
# generator = list_generator([1, 2])
# print(next(generator))
# print(next(generator))
# print(next(generator))


# def fibonacci(number):
#     a = b = 1
#     for _ in range(number):
#         yield a
#         a, b = b, a + b
#
# for num in fibonacci(10):
#     print(num)

def accumulator():
    total = 0
    while True:
        value = yield total
        print('Got: {}'.format(value))

        if not value: break
        total += value

generator = accumulator()
next(generator)
