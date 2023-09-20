# ویژیگی های محافظت شده و خصوصی-------------------------
class BankAccount:
    def __init__(self, account_number):
        self._balance = 0
        self.__account_number = account_number

    def deposit(self, value):
        self._balance = self._balance + value
        return self._balance

    def withdraw(self, value):
        if value <= self._balance:
            self._balance = self._balance - value
        else:
            raise ValueError("price cannot be negative")
        return self._balance