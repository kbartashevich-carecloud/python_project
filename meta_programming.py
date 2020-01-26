# class Class:
#     pass
#
# obj = Class()
# print(type(obj))
# print(type(Class))
#
# print(issubclass(Class, type))
# issubclass(Class, object)
#
# def dummy_factory():
#     class Class:
#         pass
#
#     return Class
#
# Dummy = dummy_factory()
# print(Dummy() is Dummy())
#
# NewClass = type('NewClass', (), {})
# print(NewClass)
# print(NewClass())

# class Meta(type):
#     def __new__(cls, name, parents, attrs):
#         print('Creating {}'.format(name))
#
#         if 'class_id' not in attrs:
#             attrs['class_id'] = name.lower()
#
#         return super().__new__(cls, name, parents, attrs)
#
# class A(metaclass=Meta):
#     pass
# print('A.class_id: {}'.format(A.class_id))

class Meta(type):
    def __init__(cls, name, bases, attrs):
        print('Initializing - {}'.format(name))

        if not hasattr(cls, 'registry'):
            cls.registry = {}
        else:
            cls.registry[name.lower()] = cls

        super().__init__(name, bases, atrs)


class Base(metaclass=Meta): pass
class A(Base): pass
class B(Base): pass