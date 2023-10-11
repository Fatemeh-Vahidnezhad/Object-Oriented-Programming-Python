class father:
    def __init__(self,name):
        self.name = name

    def first_attr(self):
        print("test")



#hierarchican inheritance: every class relates to the first class
#every child class can access and change the variable and methods of the first class
class child1(father):
    def __init__(self,name, salary):
        self.salary = salary
        father.__init__(self,name)
    def att1(self):
        father.first_attr(self)



#hierarchican inheritance: every class relates to the first class
#every child class can access and change the variable and methods of the first class
class child2(father):
    def __init__(self,name, position):
        self.position = position
        father.__init__(self,name)

    def att2(self):
        father.first_attr(self)



emp1 = child2("hamid","mng")
print(emp1.name)
emp1.att2()
