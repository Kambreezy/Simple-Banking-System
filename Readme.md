#Banking System:Mwananchi Banking
This is a Banking program written in python that defines two classes, Account and Customer, for implementing basic bank operations such as deposit, withdraw, checking balance, and applying for a loan. The Account class has methods for deposit, withdraw, getting the current balance, and applying for a loan. The Customer class inherits from the Account class and adds a method to update the balance by interacting with the user through a menu of options. The program starts by displaying a welcome message to the user and calling the updateBalance method on a newly created Customer object. The method then displays a menu of options to the user, prompts for input, and performs the selected operation. If the user chooses to apply for a loan, the method checks the current balance and returns a message indicating whether the user qualifies or not. If the user enters an invalid input, the program catches the ValueError exception and displays a message asking the user to enter a number.