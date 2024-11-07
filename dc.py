class Dog:
    def speak(self):
        return 'Woof'

class Cat:
    def speak(self):
        return 'Meow'

def animal_speak(anim):
    print(anim.speak())

dog = Dog()
cat = Cat()
dog2 = Dog()

animal_speak(dog)
animal_speak(cat)

