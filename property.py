class BankAccount:


    def __init__(self,owner_name,balance):
        self.owner_name = owner_name
        self._balance = balance

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self,value):
        if value < 0:
            raise ValueError("Balance can't be negative!")
        
        self._balance = value

acc = BankAccount("Mohamed", 1000)

print(acc.balance)     # 1000

acc.balance = 500       # تعديل صحيح
print(acc.balance)      # 500

acc.balance = -100       # المفروض يرفض!
