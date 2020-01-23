import functools

def logger(func):
    @functools.wraps(func)
    def wrapped(*args, **kwargs):
        result = func(*args, **kwargs)
        with open('log.txt', 'w') as f:
            f.write(str(result))

        return result
    return wrapped


@logger
def summator(num_list):
    return sum(num_list)


print('Summator: {}'.format(summator([1, 2, 3, 4, 5])))
print(summator.__name__)

def logger(filename):
    def decorator(func):
        def wrapped(*args, **kwargs):
            result = func(*args, **kwargs)
            with open(filename, 'w') as f:
                f.write(str(result))
            return result
        return wrapped
    return decorator

@logger('new_log.txt')
def summator(num_list):
    return sum(num_list)


def first_decorator(func):
    def wrapped():
        print('First')
        return func()
    return wrapped

def second_decorator(func):
    def wrapped():
        print('Second')
        return func()
    return wrapped


@first_decorator
@second_decorator
def decorated():
    print('Finally called...')

