from datetime import datetime

def get_seconds():
    """Return current seconds"""
    return datetime.now().second

print(get_seconds())
print(get_seconds.__doc__)
print(get_seconds.__name__)

def split_tags(tag_string):
    tag_list = []
    for tag in tag_string.split(' , '):
        tag_list.append(tag.strip())

    return tag_list

print(split_tags('python, coursera, mooc'))

def add(x: int, y: int) -> int:
    return x + y

print(add(10, 11))
print(add('still', 'works'))

def extender(source_list, extend_list):
    source_list.extend(extend_list)

values = [1, 2, 3]
extender(values, [4, 5, 6])

print(values)

def replacer(source_tuple, replace_tuple):
    source_tuple = replace_tuple

user_info = ('Guido', '31/01')
replacer(user_info, ('Larry', '27/09'))

print(user_info)

def greeting(name='default name'):
    print('Hello, {}'.format(name))

greeting()


def printer(*args):
    print(type(args))

    for argument in args:
        print(argument)

printer(1, 2, 3, 4, 5)
name_list = ['a', 'b', 'c']
printer(*name_list)


def printer(**kwargs):
    print(type(kwargs))

    for key, value in kwargs.items():
        print('{}: {}'.format(key, value))

printer(a=10, b=11)