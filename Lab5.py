#Purva Patel #100886734
class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance
        self.transaction_history = []

    def get_balance(self):
        return self.balance

    def set_balance(self, balance):
        assert isinstance(balance, int), "You must enter a number"
        assert balance > -1, "Balance cannot be negative"
        self.balance = balance

    def get_transaction_history(self):
        return self.transaction_history

    def set_transaction_history(self, transaction_history):
        self.transaction_history = transaction_history

    def get_avg_transaction(self):
        assert self.transaction_history, "No transactions have been made"
        total = sum(self.transaction_history)
        return total / len(self.transaction_history)

    def deposit(self, amount):
        assert isinstance(amount, int), "You must enter a number"
        assert amount > 0, "Error: Not greater than zero"
        self.balance = self.balance + amount
        self.transaction_history.append(amount)

    def withdraw(self, amount):
        assert isinstance(amount, int), "You must enter a number"
        assert amount > 0, "Withdrawn amount must be greater than 0"
        assert amount <= self.balance, "Error: Not greater than the balance"
        self.balance = self.balance - amount
        self.transaction_history.append(-amount)


def main():
    print("Creating the bank account:")
    bank_account = BankAccount(200)
    print("\t")
    print("Getting the average transactions (first time)")
    try:
        print(bank_account.get_avg_transaction())
    except AssertionError as assertion:
        print(assertion)
    print("\t")
    print("Depositing money")
    try:
        bank_account.deposit(-50)
    except AssertionError as assertion:
        print(assertion)
    print("\t")
    print("Depositing money")
    try:
        bank_account.deposit("not a number")
    except AssertionError as assertion:
        print(assertion)
    print("\t")
    print("Withdrawing money")
    try:
        bank_account.withdraw("not a number")
    except AssertionError as assertion:
        print(assertion)
    print("\t")
    print("Withdrawing money")
    try:
        bank_account.withdraw(300)
    except AssertionError as assertion:
        print(assertion)
    print("\t")
    print("Getting the average transactions (second time)")
    try:
        print(bank_account.get_avg_transaction())
    except AssertionError as assertion:
        print(assertion)
    print("\t")
    print("Balance:", bank_account.get_balance())

if __name__ == '__main__':
    main()