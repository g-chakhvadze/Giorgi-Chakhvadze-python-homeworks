class BankAccount:
    def __init__(self, initial_balance):
        self._balance = initial_balance

    def deposit(self, amount):
        self._balance += amount

    def withdraw(self, amount):
        if amount > self._balance:
            print("Insufficient funds")
        else:
            self._balance -= amount

    def get_balance(self):
        return self._balance


if __name__ == "__main__":
    account = BankAccount(100)

    account.deposit(50)
    print(f"Balance after deposit: {account.get_balance()}")

    account.withdraw(30)
    print(f"Balance after withdrawal: {account.get_balance()}")

    account.withdraw(150)
    print(f"Balance after failed withdrawal: {account.get_balance()}")
