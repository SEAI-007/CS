# Create and use classes and objects.
# Use methods to operate on object data.
# Organize code with functions for modularity.
# Use loops and conditionals inside functions and methods.
# Practice searching, statistics, and exit confirmation logic.


# Inside class  → self    → one account
# Outside class → accounts list → all accounts


accounts = []

def print_divider():
    print("\n" + "=" * 45)

def print_menu():
    print_divider()
    print("         Bank Account Manager")
    print_divider()
    print("  1. Create Account")
    print("  2. Deposit Money")
    print("  3. Withdraw Money")
    print("  4. View All Accounts")
    print("  5. Search Account")
    print("  6. Show Statistics")
    print("  7. Exit")
    print_divider()
    choice = input("  Enter your choice (1-7): ").strip()
    return choice

def go_back():
    choice = input("Press enter to return to the main menu.")
    if choice == "":
        return
    
# Create Account – Store account holder’s name, account number, and initial balance.
class BankAccount:
    def __init__(self, name, account_no, balance):
        self.name = name.strip().title()
        self.account_no = account_no
        self.balance = balance

    @classmethod
    def create_account(cls):
        print_divider()
        print("\n----------Add a New Account----------")
        # Name - a string that stores the account holder’s name.
        name = input("Please enter account holders name: ").strip().title()
        while name =="":
            name = input("You have to enter account holders name: ").strip().title()
        # Account Number - a string that stores the account number (ensure it’s numeric).
        account_no = input(f"Enter account number for account belonging to {name}: ").strip()
        while not account_no.isdigit():
            account_no = input("You have to enter a valid account number").strip()
        # Initial Balance - a float that stores the opening balance (ensure it’s a valid number).
        while True:
            balance_input = input("Enter the opening balance: $").strip()
            if balance_input.replace(".", "", 1).isdigit():
                balance = float(balance_input)
                if balance >= 0:
                    break
                print("Balance cannot be negative. Please enter a valid amount.")
            else:
                print("Invalid input. Please enter a valid number.")

        new_account = cls(name, account_no, balance)
        print(f"Account for {name} with account number {account_no} created successfully with a balance of ${balance}.")
        print_divider()
        print(new_account)
        go_back()
        return new_account

# Deposit Money – Add an amount to the account balance. class works on only 1 account
    def deposit (self):
        print_divider()
        print("\n----------Deposit Money----------")

        while True:
            amount_input = input("Enter deposit amount: ").strip()
            if amount_input.replace(".", "", 1).isdigit():
                amount = float(amount_input)
                break
            print("Invalid input. Please enter a valid number.")
        # if amount > 0:
        #     print("Deposit amount must be greater than 0.")
        #     return
        
        # else:
        #         print("Invalid input. Please enter a valid number.")
        if amount <= 0:
            print_divider()
            print("Deposit amount must be greater than 0.")
            return
        
        self.balance += amount
        print(f"Deposited ${amount}. New balance: ${self.balance}") 

        print_divider()
        go_back()

# Withdraw Money – Subtract an amount from the balance also class as works on one at a time.
    def withdraw (self):
        print("-----------Withdraw Money---------")

        while True:
            amount_input = input("Enter withdraw amount: ").strip()
            if amount_input.replace(".", "", 1).isdigit():
                amount = float(amount_input)
                break
            print("Invalid input. Please enter a valid number.")

        if amount <= 0:
            print_divider()
            print("Withdraw amount must be greater than 0.")
            return
        
        if amount > self.balance:
            print_divider()
            print("Insufficient funds. Withdrawal amount exceeds current balance.")
            return
        
        self.balance -= amount
        print(f"Withdraw amount ${amount}. New balance: ${self.balance}")
        print_divider()
        go_back()

# view 1 account class
    def __str__(self):
        return (
            f"\n  {'─' * 35}"
            f"\n  Holder  : {self.name}"
            f"\n  Acc No  : {self.account_no}"
            f"\n  Balance : ${self.balance:.2f}"
            f"\n  {'─' * 35}"
        )

# outside class         
# View All Accounts – Display all account details.

def view_acconts():
    print_divider()
    print("----------View all Accounts----------")

    if not accounts:
        print("\n No accounts found.")
        go_back()
        return
    
    for i, account in enumerate(accounts, start=1):
        print(f"\n Account #[i]")
        print(account)
        print_divider()
    go_back()

# Search Account by Name or Number – Case-insensitive search.
def search_accounts():
    print_divider()
    print("\n--------Search for an Account---------")

    search_by = input("Search by (name or number) ").strip().lower()
    #search_account = input("Do Want to search: name/number").strip()

    if search_by == "name":      
    #if choice.lower() == "name":
        search_name = input("Enter the name of the account holder: ").strip().title()
        found = False
        for account in accounts:
        #print(f"\nSearching results for {search_name}: ")
        #for self.name in names:
            if account.name == search_name:
                print(f" No accounts found with the name {search_name}.")
                print(account)
                found = True
                break
        if not found:
        #print(f"\nAccount holder: {account['name']}, with the account: {account['account_no']}")
            print(f"\nNo accounts found with the name {search_name}.")
            #print_divider()
            #go_back()

    elif search_by == "number":
        search_no = input("Enter the account number: ").strip()
        found = False
        #print(f"\nSearching results for {search_number}:")
        for account in accounts:
            if account.account_no == search_no:
                print("\n Account found")
                #print(f"\nAccount holder {account["name"]} with the account: {account["account_no"]}")
                print_divider()
                #go_back()
    else:
        #print("Account not found.")      ###########problem
        print("Invalid search criteria. Please choose 'name' or 'number'.")
    go_back()                                                       # If the  is found
    #print_divider()      

# Show Statistics – Total accounts, total balance, average balance.
def show_statistics():
    print_divider()
    print("\n--------Bank Statistics---------")

    total_accounts = len(accounts)
    total_balance = sum(account.balance for account in accounts)
    average_balance = total_balance / total_accounts if total_accounts > 0 else 0
    highest = max(accounts, key=lambda a: a.balance)
    lowest = min(accounts, key=lambda a: a.balance)

    print(f"Total accounts: {total_accounts}")
    print(f"Total balance: ${total_balance:.2f}")
    print(f"Average balance: ${average_balance:.2f}")
    print(f"Highest balance: {highest.name} (${highest.balance:.2f})")
    print(f"Lowest balance: {lowest.name} (${lowest.balance:.2f})")
                                           
    print_divider()
    go_back()

def find_account():
    if not accounts:
        print("No accounts found.")
        return None

    search_name = input("\nEnter the name of the account holder: ").strip().title()
    for account in accounts:
        if account.name == search_name:
            return account
    print(f"No accounts found with the name {search_name}.")
    go_back()
    return None

# Exit – Ask for confirmation before quitting.

def main():
    while True:
        choice = print_menu()

        if choice == "1":
            account = BankAccount.create_account()
            accounts.append(account)
        elif choice == "2":
            account = find_account()
            if account:
                account.deposit()
        elif choice == "3":
            account = find_account()
            if account:
                account.withdraw()
        elif choice == "4":
            view_acconts()
        elif choice == "5":
            search_accounts()
        elif choice == "6":
            show_statistics()
        elif choice == '7':
            choice = input("Are you sure you want to exit? yes/no: ").strip()
            if choice.lower() == "yes":
                print("Thank you for using the Bank Account Manager. Goodbye!")
                break
            else:
                #print("\n" + "-" * 20)
                continue
        else:
            print("Invalid choice. Please try again.")
            print("\n" + "-" * 20)

if __name__ == "__main__":
    main()






