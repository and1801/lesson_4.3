
class Animal():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_sound(self):
        print('noise')

    def eat(self):
        print('chavk')

class Bird(Animal):
    def make_sound(self):
        print('krya')

class Mammal(Animal):
    def make_sound(self):
        print('muuuu')

class Reptile(Animal):
    def make_sound(self):
        print('shhhhh')

class Zookeeper:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def feed_animal(self, animal):
        if isinstance(animal, Animal):
            print(f"{self.name} кормит {animal.name}.")
            animal.eat()
        else:
            print("Это не животное!")

class Veterinarian:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def heal_animal(self, animal):
        if isinstance(animal, Animal):
            print(f"{self.name} лечит {animal.name}.")
            
        else:
            print("Это не животное!")


b1 = Bird('ggg', 5)
a1 = Animal('rrr', 4)
m1 = Mammal('zorka', 5)
r1 = Reptile('replit-e', 5)
v1 = Veterinarian('gosh', 50)
z1 = Zookeeper('artem', 45)


z1.feed_animal(b1)
v1.heal_animal(r1)
a1.make_sound()
b1.make_sound()
m1.make_sound()
r1.make_sound()