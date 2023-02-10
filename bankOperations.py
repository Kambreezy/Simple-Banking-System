'''
@Author : Amos Kamau(Kambreezy)
About: This is a simple Banking program module that can be integrated with any banking system for basic bank operations made by any customer
'''
# Define a class named Account
class Account:
    # Define a constructor to initialize the balance to zero
    def __init__(self):
        self.Balance = 0 

    # Define a method to deposit an amount into the account
    def deposit(self, Amount):
        self.Amount = Amount
        self.Balance += Amount
        return f'Deposit successful. Current Balance is $ {self.Balance}'

    # Define a method to withdraw an amount from the account
    def withdraw(self,Amount):
        self.Amount = Amount
        # Check if the balance is sufficient for the withdrawal
        if(self.Balance >= Amount):
            self.Balance -= Amount
            return f'Withdraw successful. Current Balance is $ {self.Balance}'
        else :
            print('Insufficient Funds')
        
    # Define a method to get the current balance of the account
    def getBalance(self):
        return f'Current Balance is ${self.Balance}'

    # Define a method to apply for a loan
    def loanApplication(self):
        # Check if the balance is greater than or equal to 1000
        if self.Balance >= 1000:
            return 'You Qualify for a Loan\n Call 100 to get assisted'
        else:
            return 'Sorry, top up balance to qualify for loan'

# Define a class named Customer which inherits from Account
class Customer(Account):
    # Define a constructor to display a welcome message
    def __init__(self):
        Account.__init__(self)
        print('Welcome to Mwananchi Banking\n')

    # Define a method to update the balance based on user input
    def updateBalance(self):
        try:
            # Loop until the user chooses to exit
            while True:
                # Display a menu of options to the user
                print('0.Exit\n')
                print('1.Deposit Cash\n')
                print('2.Withdraw Cash\n')
                print('3.Check Balance\n')
                print('4.Apply for Loan\n')
                # Prompt the user for input
                choice = int(input('Enter a number between 0 and 4 \n'))

                # Perform the selected operation based on the user's choice
                if choice == 0 :
                    break
                elif choice == 1:
                    Amount = float(input('Enter amount to deposit $'))
                    print(self.deposit(Amount))
                elif choice == 2:
                    Amount = float(input('Enter amount to withdraw $'))
                    print(self.withdraw(Amount))
                elif choice == 3:
                    print(self.getBalance())
                elif choice == 4:
                    print(self.loanApplication())
                else :
                    print('Input correct numbers')
        # Catch the ValueError exception if the user enters an invalid input
        except ValueError:
            print('Enter a number only')

# Create a new Customer object and call the updateBalance method to start the program
#Uncomment the below code for testing
'''
customer = Customer()
customer.updateBalance()
'''
