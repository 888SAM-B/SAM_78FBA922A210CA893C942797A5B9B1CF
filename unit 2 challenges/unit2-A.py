class BankAccount:
    def __init__(self, account_number, account_holder_name, initial_balance):
        self._account_number = account_number
        self._account_holder_name = account_holder_name
        self._account_balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self._account_balance += amount
            print(f"{amount} deposited successfully.")
        else:
            print("Invalid amount. Deposit failed.")

    def withdraw(self, amount):
        if 0 < amount <= self._account_balance:
            self._account_balance -= amount
            print(f"{amount} withdrawn successfully.")
        else:
            print("Invalid amount or insufficient balance. Withdrawal failed.")

    def display_balance(self):
        print(f"Account Balance: {self._account_balance}")
my_account = BankAccount(123456, "John Doe", 1000.0)
my_account.display_balance()  
my_account.deposit(500.0)  
my_account.display_balance()  
my_account.withdraw(200.0)  
my_account.display_balance()  
