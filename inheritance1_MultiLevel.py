class person:
    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name

    
class employee(person):
    def __init__(self, name,age):
        self.age = age
        person.__init__(self,name)

    def get_age(self):
        return self.age


class payments(employee):
    def __init__(self, name, age, salary):
        self. salary = salary
        employee.__init__(self, name, age)

    def get_salary(self):
        return self.salary


        
        
emp1 = payments("hamid", 23, 2000)
print(emp1.salary)
