from abc import ABC, abstractmethod
class Person:
    def __init__(self, name, last_name,Birthdate):
        self.name = name
        self.last_name = last_name
        self.Birthdate = Birthdate
    def fullname(self):
        return self.name +' '+ self.last_name

class employees(Person):
    def __init__(self,name,last_name, Birthdate, department,salary,overtime=0.0):
        self.department = department
        self.salary = salary
        self.overtime = overtime
        super().__init__(name,last_name, Birthdate)


class payment(ABC):
    @abstractmethod      #using abstractmethod
    def earning(self):
        pass  #abstractmethod

class manger(employees,payment):
    def __init__(self,name,last_name, Birthdate, department, salary,overtime, employee = None):
        super().__init__(name,last_name, Birthdate, department, salary,overtime)
        if  employee == None:
            self.employee = []
        else:
            self.employee = employee

    def add_employee(self, emp):
        return self.employee.append(emp)

    def print_employees(self):
        for emp in self.employee:
            print(emp.fullname())

    def earning(self):
        return self.salary +  2 * (self.overtime)


class Devlop(employees,payment):
    def __init__(self,name,last_name, Birthdate, department, salary, overtime, language):
        super().__init__(name,last_name, Birthdate, department, salary,overtime)
        self.language = language

    def earning(self):
        return int(self.salary +  1.4 * (self.overtime))



dev1 = Devlop("reza","hamidi","20000101", "Developer",2000,5,"python")
#print(dev1.language)
mng1 = manger('Hamed',"irani", "19850112","manager",2700,20)
'''mng1.add_employee(dev1)
mng1.print_employees()'''
print(mng1.earning()) #earning method is polymorphism :  methods with same name and different parameters return result
print(dev1.earning())#earning method is abstraction:the result of a method in a class (payment) is used on another class
