class Student:
    def __del__(self):
        print("Destructor Called")

s1 = Student()
del s1