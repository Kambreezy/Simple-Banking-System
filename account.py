class BankAccount:
    def __init__(self):
        self._balance = 0

    def deposit(self, amount):
        self._balance += amount

    def withdraw(self, amount):
        if amount > self._balance:
            print("Insufficient balance")
        else:
            self._balance -= amount

    def get_balance(self):
        return self._balance

class BankUser(BankAccount):
    def __init__(self):
        BankAccount.__init__(self)

    def update_balance(self):
        while True:
            print("1. Deposit")
            print("2. Withdraw")
            print("3. Check Balance")
            print("4. Exit")
            choice = int(input("Enter your choice: "))
            if choice == 1:
                amount = float(input("Enter amount to deposit: "))
                self.deposit(amount)
                print("Balance updated successfully")
            elif choice == 2:
                amount = float(input("Enter amount to withdraw: "))
                self.withdraw(amount)
                print("Balance updated successfully")
            elif choice == 3:
                print("Your current balance is: ", self.get_balance())
            elif choice == 4:
                break
            else:
                print("Invalid choice")

user = BankUser()
user.update_balance()
