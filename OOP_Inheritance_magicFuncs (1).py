from dateutil import parser
import datetime

class Person:
    def __init__(self, name, last_name, Birthdate):
        self.name = name
        self.last_name = last_name
        self.Birthdate = Birthdate

    def fullname(self):
        return self.name.capitalize() + ' ' + self.last_name.capitalize()


class Employee(Person):
    def __init__(self, name, last_name, Birthdate, postion, hiredate, salary):
        Person.__init__(self, name, last_name, Birthdate)
        self.postion = postion
        self.hiredate = hiredate
        self.salary = salary

    def increase_salary(self,amount):
        self.salary += amount*self.salary
        return self.salary

    def __add__(self, other):
        return self.salary + other

    def __str__(self):
        return "class name is: {} ,fullname:{} , postion: {} , hiredate is: {}".format(__class__.__name__,self.fullname(), self.postion, self.hiredate)

    def duration(self):
        diff = datetime.datetime.now() -parser.parse(self.hiredate)
        return diff.days

class mng(Employee):
    #salary_mng = 0.2

    def __init__(self,name, last_name, Birthdate, postion, hiredate, salary, employees = None):
        Employee.__init__(self, name, last_name, Birthdate, postion, hiredate, salary)
        if employees == None:
            self.employees = []
        else:
            self.employees = employees


    def add_emp(self, emp):
        return self.employees.append(emp)

    def list_emp(self):
        for emp in self.employees:
            print(emp.fullname())

                           #define employees
emp1 = Employee('amir','ahmadi', '1985-10-25','Developer', '2020-01-01', 2500)
emp2 = Employee('ali','rezaee', '1985-11-20','Developer', '2021-04-01', 2900)
#print(emp1)
#print(emp1.fullname())
#print(emp1.increase_salary(0.15))
mng1 = mng("afra",'irani', '1985-10-25','manager', '2019-01-01', 6500)
                         #asign employees to a manager
mng1.add_emp(emp1)
mng1.add_emp(emp2)
#print(mng1.list_emp())
#print(mng1.increase_salary(0.2))
                         #__add__
#print(emp2.salary.__add__(emp1.salary))
                        #duration
print(emp1.duration())
