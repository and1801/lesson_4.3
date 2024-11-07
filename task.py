
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

class Zookeeper():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def feed_animal(self):
        pass

class Veterinarian():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def heal_animal(self):
        pass


b1 = Bird('ggg', 5)
a1 = Animal('rrr', 4)
m1 = Mammal('zorka', 5)
r1 = Reptile('replit', 5)
v1 = Veterinarian('gosh', 50)
z1 = Zookeeper('artem', 45)


z1.feed_animal()
v1.heal_animal()
a1.make_sound()
b1.make_sound()
m1.make_sound()
r1.make_sound()