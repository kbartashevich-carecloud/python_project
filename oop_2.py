class Pet:
    def __init__(self, name=None):
        self.name = name

class Dog(Pet):
    def __init__(self, name, breed=None):
        super().__init__(name)
        self.breed = breed

    def say(self):
        return "{0}: waw".format(self.name)

dog = Dog("Jack", "Doberman")
print(dog.name)
print(dog.say())

import json

class ExportJSON:
    def to_json(self):
        return json.dumps({
            "name": self.name,
            "breed": self.breed
        })

class ExDog(Dog, ExportJSON):
    def __init__(self, name, breed=None):
        super().__init__(name, breed)

class WoolenDog(Dog, ExportJSON):
    def __init__(self, name, breed=None):
        super(Dog, self).__init__(name)
        self.breed = "new kind of dogs"

dog = WoolenDog("Jack", breed="Taksa")
print(dog.breed)

class Dog(Pet):
    def __init__(self, name, breed=None):
        super().__init__(name)
        self.__breed = breed

    def say(self):
        return "{0}: waw!".format(self.name)

    def get_breed(self):
        return self.__breed




