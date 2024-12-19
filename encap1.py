# Encapsulation :- with the help of Encapsulation we can deside that what kind of attribute show or hide as well as protect

class BankingAccount:

    def __init__(self,owner,balance =0):
        self.owner = owner
        self.__balance = balance


    def deposite(self,amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposite: {amount}.Available Balance: {self.__balance}")
        else:
            print("No transaction")


    def withdraw(self,amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Debited amount: {amount},Available balance: {self.__balance} ")
        else:
            print("Insufficient Balance, Try next time...")


    def get_balance(self):
        return(self.__balance)

ac = BankingAccount("Mac",75500)
ac.deposite(25000)
ac.withdraw(500)
print(f"Available Balance:{ac.get_balance()}")
print()
