class BankAccount:
    def __init__(self, balance:float):
        self.__balance = balance
    def get_balance(self):
        return self.__balance
    def deposit(self, amount):
        self.__balance = self.__balance - amount
    

class CheckingAccount(BankAccount):
    def __init__(self, balance):
        super().__init__(balance) #perlu kah ini?
        self.transaction_count = 0 #perlu, karena ada instance variabel baru

    #increment: gimana caranya modif deposit(), withdraw(), transfer()
    # OVERRIDING method:
    def deposit(self, amount):
        self,transaction_count += 1
        super().deposit(amount) #kalo self.deposit(), berarti dia refer ke diannya sendiri (rekursi), nanti jd ambigu
    def withdraw(self, amount):
        self,transaction_count += 1
        super().withdraw(amount) 
    def transfer(self, amount, other):
        self,transaction_count += 1
        super().transfer(amount) 

#STEP 2: 
    def __init__(self, balance, free_transaction=2, fee=100): #yg deafult harus ditaro paling kanan
        super().__init__(balance) 
        self.transaction_count = 0
        self.free_transaction = free_transaction
        self.transaction_fee = fee

    def deduct_fee(self):
        if self.transaction_count > self.free_transaction:
            self.balance -= self.transaction_fee*(self.transaction_count - self.free_transaction)
