class Animal:
    def sound(self):
        pass

class Dog(Animal):
    def sound(self):
        print("Dog barks")

class Cat(Animal):
    def sound(self):
        print("Cat meows")

def factory(name):
    if name == "dog":
        return Dog()
    elif name == "cat":
        return Cat()

a = factory("dog")
a.sound()

b = factory("cat")
b.sound()