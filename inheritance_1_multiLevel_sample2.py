class Person:
    def __init__(self, name, last_name ,id):
        self.name = name
        self.last_name = last_name
        self.id = id

    def fullname(self):
        return (self.name.capitalize() + ' '+ self.last_name.capitalize())
    

class Employee(Person):
    def __init__(self, name, last_name, id, salary, position):
        self.salary = salary
        self.position  = position
        Person.__init__(self, name,last_name, id)


class manager(Employee):


    def __init__(self, name,last_name, id, salary, position = 'mng',employees = None):

        if employees == None:
            employees = []
        else:
            self.employees = employees
        Employee.__init__(self, name, last_name, id, salary,position = 'mng' )
        

        
    def add_emp(self,emp):
        self.employees.append(emp)

    def remove_emp(self,emp):
        self.employees.remove(emp)

    def print_employees(self):
        for emp in self.employees:
            print('the list of employees:',emp.fullname(),emp.position)
        




emp1 = Employee('ali','rezaeei',12,4300,'developer')
emp2 = Employee('mina','irani',111,5300,'developer')

emp1.fullname()
mng1 = manager('hamid','sadeghi', 23,7200,'mng',[emp1])
mng1.add_emp(emp2) 
mng1.print_employees()



