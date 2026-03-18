""" Simple Bank Account Manager
Goal:
Build a Python program to manage simple bank accounts, practicing:

String manipulation

Lists, tuples, sets, dictionaries

Conditionals (if/elif/else)

Loops (while, for, nested loops)

Functions

Classes and objects

Exit confirmation

📊 Learning Objectives
Create and use classes and objects.

Use methods to operate on object data.

Organize code with functions for modularity.

Use loops and conditionals inside functions and methods.

Practice searching, statistics, and exit confirmation logic.

📌 Features to Implement
Create Account – Store account holder’s name, account number, and initial balance.

Deposit Money – Add an amount to the account balance.

Withdraw Money – Subtract an amount from the balance (check for insufficient funds).

View All Accounts – Display all account details.

Search Account by Name or Number – Case-insensitive search.

Show Statistics – Total accounts, total balance, average balance.

Exit – Ask for confirmation before quitting.

📂 Data Structures
Class BankAccount with attributes:

class BankAccount:

           def __init__(self, name, account_number,
           balance):

                         self.name = name

                         self.account_number = account_number

                         self.balance = balance
List → stores all BankAccount objects.

Set → optional, to store unique account numbers.

📜 Menu System
The program should output 7 options to the user:

               1. Create Account
               2. Deposit Money
               3. Withdraw Money
               4. View All Accounts
               5. Search Account
               6. Show Statistics
               7. Exit

Then, it has to:

Ask the user to enter the number of the action it wishes to carry out.

If the number is not in the range 1 to 7, send and error message and ask for a correct option and keep looping this action until the user chooses an option in the list.

If the number is in the range 1 to 7 redirect them to the correct block of code.

🛠 Classes and Functions to Create
Class BankAccount

Attributes: name, account_number, balance.

Methods:

deposit(amount) → adds to balance

withdraw(amount) → subtracts from balance if sufficient funds

display() → prints account info

create_account(accounts_list)

Ask for name → format with .title().

Ask for account number → validate uniqueness.

Ask for initial balance → validate as number.

Create BankAccount object and append to list.

deposit_to_account(accounts_list)

Ask for account number.

Search and deposit amount using the deposit method.

withdraw_from_account(accounts_list)

Ask for account number.

Search and withdraw amount using the withdraw method.

view_all_accounts(accounts_list)

Loop through accounts and call each account’s display() method.

search_account(accounts_list, query)

Search by name or account number (case-insensitive).

Display account info if found.

show_statistics(accounts_list)

Total accounts (len(accounts_list)).

Total balance (sum of balances).

Average balance.

confirm_exit()

Ask "Are you sure you want to exit? (yes/no)".

Return True if yes, otherwise False."""

print("Welcome to the Simple Bank Account Manager!")