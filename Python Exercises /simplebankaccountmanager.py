def menu_system():
    accounts_list = []
    query = ""
    user_input = ""
    while user_input != "quit:":
        print("""\n1. Create Account
               \n2. Deposit Money
               \n3. Withdraw Money
               \n4. View All Accounts
               \n5. Search Account
               \n6. Show Statistics
               \n7. Exit""")
        choice = input("Enter a number to carry out the wanted action: ")
        if choice == "1":
            create_account(accounts_list)
        elif choice == "2":
            deposit_to_account(accounts_list)
        elif choice == "3":
            withdraw_from_account(accounts_list)
        elif choice == "4":
            view_all_accounts(accounts_list)
        elif choice == "5":
            try:
                query = int(input("Input your account number please: "))
                search_account(accounts_list, query)
            except:
                print("Please enter a number and try again.")
        elif choice == "6":
            show_statistics(accounts_list)
        elif choice == "7":
            if confirm_exit():
                return
        else:
            print("Please input a valid number between 1 and 7")

class BankAccount:
    def __init__(self, name, account_number, balance):
        self.name = name
        self.account_number = account_number
        self.balance = balance
    def __str__(self):
        return(f"{self.name},{self.account_number},{self.balance}")
    def deposit(self,amount):
        self.balance += amount
    
    def withdraw(self, amount):
        self.balance -= amount

    def display(self):
        print(self.name,self.account_number,self.balance)

def create_account(accounts_list):
        name = input("Input name please: ").title()
        try:
            account_number = int(input("Input account number please: "))
        except:
            print("Please insert a number only and try again")
            return
        account_number_unique = False
        while account_number_unique == False:
            for account in accounts_list:
                if account.account_number != account_number:
                    pass
                else:
                    print("Account number is already taken, try to create a new account again with a different number")
                    return
            account_number_unique = True

        initial_balance = 0
        user_input = ""
        while user_input != "quit":
            try:
                initial_balance = int(input("Insert a balance: "))
                user_input = "quit"
            except:
                print("Please enter a number.")
        accounts_list.append(BankAccount(name,account_number,initial_balance))

def deposit_to_account(accounts_list):
    account_number = ""
    try:
        account_number = int(input("Input your account number please"))
    except:
        print("Please input a real number")
        return
    for account in accounts_list:
        if account.account_number == account_number:
            try:
                account.balance += int(input("How much do you want to deposit? "))
            except:
                print("A valid number is required")
        else:
            print("Account couldn't be found")

def withdraw_from_account(accounts_list):
    account_number = ""
    try:
        account_number = int(input("Input your account number please"))
    except:
        print("Please input a real number")
        return
    for account in accounts_list:
        if account.account_number == account_number:
            try:
                account.balance -= int(input("How much do you want to withdraw? "))
            except:
                print("A valid number is required")
        else:
            print("Account couldn't be found")

def view_all_accounts(accounts_list):
    for account in accounts_list:
        print(account)

def search_account(accounts_list, query):
    for account in accounts_list:
        if account.account_number == query:
            print(account)
        else:
            print("account couldn't be found.")

def show_statistics(accounts_list):
    print(f"total number of accounts {len(accounts_list)}")
    total_balance = 0
    for account in accounts_list:
        total_balance += account.balance
    print(f"Total balance of all accounts: {total_balance}")
    print(f"Average balance per account {total_balance/len(accounts_list)}")

def confirm_exit():
    choice = input("Are you sure you want to exit? (y/n) ")
    if choice == "y":
        return True
    else:
        return False
    
menu_system()