class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount
        
    def withdraw(self, amount): 
        if amount > self.balance:
            return "-1"
        else:
            self.balance -= amount
            return 0
    def __str__(self):
        return f"""Account Number: **{self.account_number:2f}
        Balance: {self.balance:.2f}"""