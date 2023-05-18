class User:
    def __init__(self, name, age, int_rate):
        self.name = name
        self.int_rate = int_rate
        self.age = age
        
    def show_details(self):
        return f"Thank you, {self.name.title()}, ({self.age} years old)"


class Bank(User):
    total_deposits = 0
    total_withdraws = 0


    def __init__(self, name, age, balance):
        super().__init__(name, age, int_rate)
        self.balance = balance


    def show_info(self):
        return f"{self.name} has a remaining balance of: ${round(self.balance, 2)}"


    def deposit(self):
        dp = float(input(f"{self.name.title()}, please enter how much you would like to deposit: "))
        print("Thank you for depositing...")
        self.balance += dp
        self.total_deposits += 1
        self.balance = (float(self.int_rate) * (dp)) + self.balance
        return f"Your balance is now ; {round(self.balance, 2)} with a {float(self.int_rate)}% intrest rate. "


    def withdraws(self):
        wd = float(input(f"{self.name.title()}, please enter how much you would like to withdraw: "))
        if self.balance < wd:
            return "You can't withdraw that amount.."
        else:
            print("Thank you for withdrawing...")
            self.balance -= wd
            self.total_withdraws += 1
            return f"Your Balance is now: {round(self.balance, 2)}"


def options(user_two):
    print("Thank you for creating your bank account")
    print("Here are a list of options, please choose the number you want")
    while True:
        option_choice = int(input("1) See Balance\n2) Withdraw\n3) Deposit\n4) See Total Withdraws\n5) See Total Deposits\n6) Quit\n"))
        if option_choice == 1:
            print(user_one.bank.show_info())
            if option_choice == 1 and user_two != None:
                print(user_two.bank.show_info())
        elif option_choice == 2:
            print(user_one.bank.withdraws())
            if option_choice == 2 and user_two != None:
                wd = input(f"{user_two.name} would you like to withdraw? Yes or No: ")
                if wd.lower() == 'yes':
                    print(user_two.bank.withdraws())
        elif option_choice == 3:
            print(user_one.bank.deposit())
            if option_choice == 3 and user_two != None:
                dep = input(f"{user_two.name} would you like to deposit? Yes or No: ")
                if dep.lower() == 'yes':
                    print(user_two.bank.deposit())
        elif option_choice == 4:
            print(f"There have been {user_one.bank.total_withdraws} withdraws.")
            if option_choice == 4 and user_two != None:
                print(f"There have been {user_two.bank.total_withdraws} withdraws.")
        elif option_choice == 5:
            print(f"There have been {user_one.bank.total_deposits} deposits. ")
            if option_choice == 5 and user_two != None:
                print(f"There have been {user_two.bank.total_deposits} deposits. ")
        elif option_choice == 6:
            print("Thank You for using York Bank.")
            return False
            break
        else:
            print("Please choose a number 1-6.")


def bank_creation(name):
    balance = float(input(f"{name.title()}, how much money do you have? "))
    return balance


while True:
    print("Welcome to York Bank")
    name = input("Enter your name: ")
    age = input("Enter your age: ")
    int_rate = input("Enter what intrest rate you would like: ")
    user_one = User(name, age, int_rate)
    user_two = None
    new_user = input("Would you like to register a new person? Type 'no' to create your bank: ")
    if new_user.lower() == 'yes':
        name = input("Enter the second person's name: ")
        age = int(input("Enter the second person's age: "))
        user_two = User(name, age, int_rate)
        print("Thank you for registring 2 people. Please create your bank accounts. ")
        user_one.balance = bank_creation(user_one.name)
        user_two.balance = bank_creation(user_two.name)
        user_one.bank = Bank(user_one.name, user_one.age, user_one.balance)
        user_two.bank = Bank(user_two.name, user_two.age, user_two.balance)
        flag = options(user_two)
        if flag == False:
            break
        
    else:
        user_one.balance = bank_creation(user_one.name)
        user_one.bank = Bank(user_one.name, user_one.age, user_one.balance)
        flag = options(user_two)
        if flag == False:
            break


# I spent too much time on this one, I was having fun with it though. 