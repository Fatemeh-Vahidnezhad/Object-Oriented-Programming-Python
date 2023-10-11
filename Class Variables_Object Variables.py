class employee():
    
    pay_raising = 0.1
    
    def __init__(self, first,last,pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

   #this the sample of instace(object) method, it takes self as an argument 
    def full_name(self):
        return '{} {}'.format(self.first.capitalize() , self.last.capitalize())

    def pay_increase(self):
        self.pay += self.pay * self.pay_raising
        return self.pay
        


emp1 = employee('ali','ahmadi',2000)
emp2 = employee('Reza' , 'sadeghi',2500)

print(emp1.email)
print(emp2.full_name())
#using self with class variables like pay_raising,overwrite the class variable for that especial object.
#IF we use employee.pay_raising, the amount of pay_raising will not change for any object.
emp1.pay_raising = 0.2  
print(emp1.pay_raising)
print(emp1.pay_increase())
print(emp2.pay_increase())
