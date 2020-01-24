class Planet:

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

    def __repr__(self):
        return f"Planet {self.name}"

earth = Planet("Earth")
print(earth)

solar_system = []

planet_names = [
    "Mercury", "Venus", "Earth", "Mars",
    "Jupiter", "Saturn", "Uranus", "Neptune"
]

for name in planet_names:
    planet = Planet(name)
    solar_system.append(planet)

print(solar_system)

class Planet:

    count = 0

    def __init__(self, name, population=None):
        self.name = name
        self.population = population or []
        Planet.count += 1

earth = Planet("Earth")
mars = Planet("Mars")

print(Planet.count)
print(mars.count)

class Human:

    def __del__(self):
        print("Goodbye!")

human = Human()
del human

class Planet:
    """This class describes planets"""

    count = 1

    def __init__(self, name, population=None):
        self.name = name
        self.population = population or []


planet = Planet("Earth")
print(planet.__dict__)

planet.mass = 5.97e24
print(planet.__dict__)

print(Planet.__dict__)
print(planet.__class__)


class Planet:

    def __new__(cls, *args, **kwargs):
        print("__new__ called")
        obj = super().__new__(cls)
        return obj

    def __init__(self, name):
        print("__init__ called")
        self.name = name

earth = Planet("Earth")


class Human:

    def __init__(self, name, age=0):
        self._name = name
        self._age = age

    def _say(self, text):
        print(text)

    def say_name(self):
        self._say(f"Hello, I am {self._name}")

    def say_how_old(self):
        self._say(f"I am {self._age} years old")


class Planet:

    def __init__(self, name, population=None):
        self.name = name
        self.population = population or []

    def add_human(self, human):
        print(f"Welcome to {self.name}, {human.name}")
        self.population.append(human)


mars = Planet("Mars")
bob = Human("Bob")
mars.add_human(bob)
print(mars.population)
