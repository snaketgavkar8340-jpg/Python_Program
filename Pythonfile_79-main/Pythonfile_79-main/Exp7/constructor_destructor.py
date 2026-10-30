class Student:
    def __init__(self, name):
        self.name = name
        print("Constructor Called")

    def display(self):
        print("Name:", self.name)

    def __del__(self):
        print("Destructor Called")

s1 = Student("Rahul")
s1.display()
del s1