import datetime
class Employee():
    def __init__(self,name,age,salary):
        self.name = name
        self.age = age
        self.salary = salary
        self.mail = name + '@company.com'

#using classmethod to return an object
    @classmethod
    def seperator(cls, str_fiture):
        name, age,salary = str_fiture.split("-")
        return Employee(name, age,salary)

#utility function or static function does not have a direct relation with class and objects 
    @staticmethod    
    def week_day(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True
        
        



emp1 ="Hassan-26-2000"
empp = Employee.seperator(emp1)
print(empp.name)
print(empp.mail)
print(empp.salary)
day = datetime.date(2020,12,6)
print(Employee.week_day(day))

