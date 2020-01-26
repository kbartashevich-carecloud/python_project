class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def __str__(self):
        return '{} <{}>'.format(self.name, self.email)

    def __hash__(self):
        return hash(self.email)

    def __eq__(self, obj):
        return self.email == obj.email

    def get_email_data(self):
        return {
            "name": self.name,
            "email": self.email
        }


jane = User('Jane Doe', 'jdoe@example.com')
joe = User('Joe Doe', 'jdoe@example.com')
print(jane.get_email_data())

class Singleton:
    instance = None

    def __new__(cls):
        if cls.instance is None:
            cls.instance = super().__new__(cls)

        return cls.instance

a = Singleton()
b = Singleton()

print(a is b)
print(jane)
print(jane == joe)


user_email_map = {user: user.name for user in [jane, joe]}
print(user_email_map)


class Researcher:
    def __getattr__(self, name):
        return '%s field was not found' % name

    def __getattribute__(self, name):
        return 'nope'


obj = Researcher()
print(obj.attr)
print(obj.method)
print(obj.dfdfdfdfd)