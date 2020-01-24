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

class PetExport:
    def export(self, dog):
        raise NotImplementedError


class ExportXML(PetExport):
    def export(self, dog):
        return """<?xml version="1.0" encoding="utf-8"?>
               <dog>
              <name>{0}</name>
              <breed>{1}</breed>
              </dog>""".format(dog.name, dog.breed)

class ExportJSON(PetExport):
    def export(self, dog):
        return json.dumps({
            "name": dog.name,
            "breed": dog.breed
        })

class Pet:
    def __init__(self, name):
        self,name = name
class Dog(Pet):
    def __init__(self, name, breed=None):
        super().__init__(name)
        self.breed = breed

class ExDog(Dog):
    def __init__(self, name, breed=None, exporter=None):
        super().__init__(name, breed)
        self._exporter = exporter or ExportJSON()

        if not isinstance(self._exporter, PetExport):
            raise ValueError("bad export instance value", exporter)

    def export(self):
        return self._exporter.export(self)


dog = ExDog("Jack", "Street", exporter=ExportXML())
dog.export()


