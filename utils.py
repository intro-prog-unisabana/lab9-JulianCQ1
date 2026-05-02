from person import Person   
from bank_account import BankAccount
def person_data():
    name = input("\n")
    person_object = Person(name)
    while True:
        account_number = input("\n")
        balance = float(input("\n"))
        account = BankAccount(account_number, balance)
        person_object.add_account(account)
        done = input("Are you done adding accounts? (yes/no):\n").lower()
        if done == "yes":
            break
    return person_object
