class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.__balance = balance      

    @property
    def balance(self):                  
        return self.__balance

    def deposit(self, amount):
        if amount <= 0:
            print("Deposit must be more than 0")
        else:
            self.__balance += amount
            print("Deposited", amount)

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdraw must be more than 0")
        elif amount > self.__balance:
            print("Not enough balance")
        else:
            self.__balance -= amount
            print("Withdrew", amount)

    def __str__(self):                  
        return "Owner: " + self.owner + " | Balance: Rs " + str(self.__balance)

    def __repr__(self):
        return "BankAccount('" + self.owner + "', " + str(self.__balance) + ")"

acc = BankAccount("Ali", 5000)
acc.deposit(1500)
acc.withdraw(2000)
acc.withdraw(100000)       
acc.deposit(-50)           
print(acc)
print(repr(acc))
print(acc.balance)         

try:
    acc.balance = 99999    
except AttributeError:
    print("Balance cannot be changed directly")
try:
    print(acc.__balance)   
except AttributeError:
    print("Balance is private")
