class BankAccount:
    def __init__(self, user_name, balance=0):
        self.user_name = user_name
        self.balance = balance
        self.history = []

    def check_balance(self):
        print(f"\n💰 {self.user_name}'s current balance: {self.balance}")

    def deposit(self):
        try:
            amount = int(input("Enter amount to deposit: "))
            if amount <= 0:
                print("❌ Amount must be greater than 0")
                return
            self.balance += amount
            self.history.append(f"Deposited: {amount}")
            print(f"✅ Deposited {amount}. New balance: {self.balance}")
        except:
            print("❌ Invalid input")

    def withdraw(self):
        try:
            amount = int(input("Enter amount to withdraw: "))
            if amount > self.balance:
                print("❌ Insufficient balance!")
            elif amount <= 0:
                print("❌ Amount must be greater than 0")
            else:
                self.balance -= amount
                self.history.append(f"Withdrawn: {amount}")
                print(f"✅ Withdrawn {amount}. Remaining balance: {self.balance}")
        except:
            print("❌ Invalid input")

    def show_history(self):
        print("\n📜 Transaction History:")
        if not self.history:
            print("No transactions yet.")
        else:
            for item in self.history:
                print("-", item)


print("🏦 Welcome to Simple Bank System")

user_name = input("Enter your name: ")
try:
    balance = int(input("Enter initial balance: "))
except:
    balance = 0

account = BankAccount(user_name, balance)

while True:
    print("\nChoose an option:")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Show History")
    print("5. Exit")

    choice = input("Enter choice (1-5): ")

    if choice == "1":
        account.deposit()
    elif choice == "2":
        account.withdraw()
    elif choice == "3":
        account.check_balance()
    elif choice == "4":
        account.show_history()
    elif choice == "5":
        print("👋 Thank you for using the bank system!")
        break
    else:
        print("❌ Invalid choice")
