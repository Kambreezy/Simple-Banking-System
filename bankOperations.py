class BankAccount:
    def __init__(self):
        self.Balance= 0 

    def depositCash(self, Amount):
        self.Balance += Amount
        return f"Deposit was successful.\n Your Balance is now {self.Balance}"

    def withdrawCash(self, Amount):
        if self.Balance > Amount:
            self.Balance -= Amount
            return f"Withdraw was successful.\n Your Balance is now {self.Balance}"
        else :
            return "Insufficient Funds"

    def checkBal(self):
        return f"Current Balance is KES {self.Balance}"

class CreateAccount(BankAccount):
    def __init__(self):
        BankAccount.__init__(self)

    def currentBal(self, Amount):
        message = super().depositCash(Amount)
        print(f"{message}\n")
        print(super().checkBal())

    
