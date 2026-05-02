class person:
    def __init__(self,name,accounts):
        self.name = name
        self.accounts = accounts
    def add_account(self, account):
        self.accounts.append(account)
    def __str__(self):
        return f"Name = {self.name}, Number of accounts = {len(self.accounts)}"
