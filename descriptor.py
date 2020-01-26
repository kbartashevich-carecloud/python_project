class Descriptor:
    def __get__(self, obj, obj_type):
        print('get')

    def __set__(self, obj, obj_type):
        print('set')

    def __delete__(self, obj):
        print('delete')

class Class:
    attr = Descriptor()

instance = Class()
instance.attr
instance.attr = 10
del instance.attr

class Value:
    def __init__(self):
        self.value = None

    @staticmethod
    def _prepare_value(value):
        return value * 10

    def __get__(self, obj, obj_type):
        return self.value

    def __set__(self, obj, value):
        self.value = self._prepare_value(value)

class Class:
    attr = Value()

instance = Class()
instance.attr = 10

print(instance.attr)

class ImportantValue:
    def __init__(self, amount):
        self.amount = amount

    def __get__(self, obj, obj_type):
        return self.amount

    def __set__(self, obj, value):
        with open('log.txt', 'w') as f:
            f.write(str(value))

        self.amount = value


class Account:
    amount = ImportantValue(100)

bobs_account = Account()
bobs_account.amount = 200

with open('log.txt', 'r') as f:
    print(f.read())

class Class:
    def method(self):
        pass

obj = Class()

print(obj.method)
print(Class.method)

class User:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'

amy = User('Amy', 'Jones')

print(amy.full_name)
print(User.full_name)

class Property:
    def __init__(self, getter):
        self.getter = getter

    def __get__(self, obj, obj_type=None):
        if obj is None:
            return self

        return self.getter(obj)

class Class:
    @property
    def original(self):
        return 'original'

    @Property
    def custom_sugar(self):
        return 'custom sugar'

    def custom_pure(self):
        return 'custom_pure'

    custom_pure = Property(custom_pure)

obj = Class()

print(obj.original)
print(obj.custom_sugar)
print(obj.custom_pure)

class StaticMethod:
    def __init__(self, func):
        self.func = func

    def __get__(self, obj, obj_type=None):
        return self.func

class Class:
    __slots__ = ['anakin']

    def __init__(self):
        self.anakin = 'the chosen one'

obj = Class()

obj.luke = 'the chosen too'