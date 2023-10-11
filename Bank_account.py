class Bank_account:
    default_accNumber = 1

    def __init__(self, name,national_id, balance=0):
        self.name = name
        self.national_id = national_id
        self.balance = balance
        self.default_accNumber = Bank_account.default_accNumber
        Bank_account.default_accNumber = Bank_account.default_accNumber + 1   #update the default bank account for the next account of the customer

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount >= self.balance:
            print("customer does not have deposit!")
            return
        self.balance -= amount

    def getBalance(self):
        print('the deposit of the customer is', self.balance)


person1 = Bank_account('Hamid',202220345)
person1.deposit(100)
person1.deposit(100)
person1.deposit(100)
person1.withdraw(100)
person1.getBalance()
print(person1.default_accNumber)
person1 = Bank_account('Hamid',202220345,220)
print(person1.default_accNumber)
person1.getBalance()
person2 = Bank_account('Reza',2022020345)
print(person2.default_accNumber)
