from datetime import date
class person():
    variable1 = 0.1
    def __init__(self,first, age,pay):
        self.name = first
        self.age = age
        self.pay = pay


#classmethod return an object to the class
    @classmethod
    def myclassMethod(cls, name, birthdate,pay): 
        return cls(name, date.today().year -birthdate,pay)#==(name,age) in __init__


#classmethod can change the class variable
    @classmethod
    def change_class_vairable(cls, amnt):
        cls.variable1 = amnt
        
        

#staticmethod cannot accept orguments of class and object
    @staticmethod
    def mystaticMethod(myage): 
        if myage > 18:
            return "Adult"
        else:
            return "child"

#object methods:
    def pay_increase(self):
        self.pay += int(self.pay * self.variable1)




            
person1 = person("ali", 29,2000)
print(person1.mystaticMethod(12))
person2 = person.myclassMethod('Reza',1993,2300)

print(person2.name)
print(person2.age)

person.change_class_vairable(0.34)  #change the value of class variable
print(person1.__dict__)
person1.pay_increase()
print(person1.pay) #pay 34 percent increased.
print('the class variable changed to:',person1.variable1)

        
        
