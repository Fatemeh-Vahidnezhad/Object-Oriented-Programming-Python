class father:
    var_father = ""

class mother:
    var_mother = ""


#child class access to the class variables on the class of father and mother and it can change them
class son(father, mother):
    def print(self):
        print("father variable:" , self.var_father)
        print("mother variable:", self.var_mother)

obj1 = son()
obj1.var_father = "test1"
obj1.var_mother = "test2"

obj1.print()
