class Student:
    def __init__(self, name):
        self.name = name

    def display(self):
        print("Name:", self.name)

s1 = Student("Rahul")
s2 = Student("Amit")

s1.display()
s2.display()