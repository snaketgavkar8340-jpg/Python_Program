class OldSystem:
    def old_method(self):
        return "Old system working"

class Adapter:
    def __init__(self, obj):
        self.obj = obj

    def new_method(self):
        return self.obj.old_method()

a = Adapter(OldSystem())
print(a.new_method())