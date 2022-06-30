class Vet:
    animals = []
    space = 5

    def __init__(self, name):
        self.name = name
        self.animals = []

    def register_animal(self, pet_name):
        if len(Vet.animals) < Vet.space:
            self.animals.append(pet_name)
            Vet.animals.append(pet_name)
            return f"{pet_name} registered in the clinic"
        return "Not enough space"

    def unregister_animal(self, pet_name):
        if pet_name in Vet.animals:
            self.animals.remove(pet_name)
            Vet.animals.remove(pet_name)
            return f"{pet_name} unregistered successfully"
        return f"{pet_name} not in the clinic"

    def info(self):
        return f"{self.name} has {len(self.animals)} animals. {Vet.space - len(Vet.animals)} space left in clinic"


peter = Vet("Peter")
george = Vet("George")
print(peter.register_animal("Tom"))
print(george.register_animal("Cory"))
print(peter.register_animal("Fishy"))
print(peter.register_animal("Bobby"))
print(george.register_animal("Kay"))
print(george.unregister_animal("Cory"))
print(peter.register_animal("Silky"))
print(peter.unregister_animal("Molly"))
print(peter.unregister_animal("Tom"))
print(peter.info())
print(george.info())