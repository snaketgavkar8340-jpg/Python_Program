class Observer:
    def update(self, message):
        print(message)

class Subject:
    def __init__(self):
        self.observers = []

    def attach(self, observer):
        self.observers.append(observer)

    def notify(self, message):
        for observer in self.observers:
            observer.update(message)

s = Subject()
o = Observer()
s.attach(o)
s.notify("New notification received")