from abc import ABC, abstractmethod


class Supply(ABC):
    @abstractmethod
    def __init__(self, name, energy):
        self.name = name
        self.energy = energy

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value == "":
            raise ValueError("Name cannot be an empty string.")
        self.__name = value

    @property
    def energy(self):
        return self.__energy

    @energy.setter
    def energy(self, value):
        if value < 0:
            raise ValueError("Energy cannot be less than zero.")
        if value > 100:
            raise ValueError("Energy cannot more than 100.")

        self.__energy = value

    def details(self):
        return f"{self.__class__.__name__}: {self.name}, {self.energy}"

# a = Supply("asd", 111)
# print(a.details())