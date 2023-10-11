class supperclass1:
    def __init__(self):
        self.name = 'hamid'
        print("supper class1")

class supperclass2:
    def __init__(self):
        self.name1 = 'reza'
        print("super class2")

class subclass(supperclass1, supperclass2):
    def __init__(self):
        supperclass1.__init__(self)
        supperclass2.__init__(self)

    def print(self):
        print("subclass",self.name)
        print("subclass",self.name1)



obj = subclass()
obj.name = "test"

obj.print()
