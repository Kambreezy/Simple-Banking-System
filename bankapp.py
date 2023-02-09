import bankOperations

print("Welcome to Mwananchi Banking. ")
firstname = input("Enter your firstname: ")
lastname = input("Enter your lastname: ")

try:
    while True:
        print("\n Please choose from the following menu: \n 0.Exit \n 1.Create Account \n 2. Check Balance \n 3.Withdraw Cash \n 4.Deposit Cash \n 5. Apply for Loan")
        customerChoice = int(input("Enter a number between 1 and 4 "))
        if customerChoice == 1 : #create account method
            print("Create Account..")
            Amount = float(input("Amount to Deposit: "))
            newAccount = bankOperations.CreateAccount()
            newAccount.greetUser(firstname,lastname)
            print(newAccount.currentBal(Amount))
        
        elif customerChoice == 2: #check balance method
            print("Checking Balance...")
            newCheck = bankOperations.Customer()
            print(newCheck.checkBal())

        elif customerChoice == 3 : #withdraw cash
            print("Withdraw cash...")



        elif customerChoice == 4 : #Loan Application
            print("Apply for a Loan...")

        elif customerChoice == 0:
            print("Exiting Program..")
            break

except ValueError:
    print('Use numbers only')