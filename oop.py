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
        print(f"Welcome to {self.name}, {human._name}")
        self.population.append(human)


mars = Planet("Mars")
bob = Human("Bob")
mars.add_human(bob)
print(mars.population)

class Event:

    def __init__(self, description, event_date):
        self.description = description
        self.date = event_date

    def __str__(self):
        return f"Event \"{self.description}\" at {self.date}"

    @classmethod
    def from_string(cls, user_input):
        description = extract_description(user_input)
        date = extract_date(user_input)
        return cls(description, date)

def extract_description(user_string):
    return "открытие чемпионата мира по футболу"


def extract_date(user_string):
    return date(2018, 6, 14)

from datetime import date

event_description = "Tell something new"
event_date = date.today()

event = Event(event_description, event_date)
print(event)


event = Event.from_string("""добавить в мой календарь открытие
чемпионата мира по футболу на 14 июня 2018 года""")
print(event)


print(dict.fromkeys("12345"))

class Human:

    def __init__(self, name, age=0):
        self.name = name
        self.age = age

    @staticmethod
    def is_age_valid(age):
        return 0 < age < 150

print(Human.is_age_valid(35))

human = Human("Old Bobby")
print(human.is_age_valid(234))


class Robot:

    def __init__(self, power):
        self._power = power

    power = property()

    @power.setter
    def power(self, value):
        if value < 0:
            self._power = 0
        else:
            self._power = value

    @power.getter
    def power(self):
        return self._power

    @power.deleter
    def power(self):
        print("Make robot useless")
        del self._power

wall_e = Robot(100)
wall_e.power = -20
print(wall_e.power)
del wall_e.power


class Robot:
    def __init__(self, power):
        self.power = power

    @property
    def power(self):
        return self._power

wall_e = Robot(200)
wall_e.power

