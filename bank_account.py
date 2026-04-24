

class bankaccount:
    def __init__(self,user_name,balance):
        self.user_name=user_name
        self.balance=balance
    def check_balance(self):
      print  ((f"the balance of account with {self.user_name} is {self.balance}"))

    def withdrawl(self):
        amount=int(input("enter the amount to withdraw::"))
        if amount >self.balance:
            print( "insufficient balance!!")
        else:
            self.balance-= amount
            print(f"{amount} has been withdrawn from account of {self.user_name} and the remaning balance is {self.balance}")

    def deposit(self):
        amount=int(input("enter the amount you want to deposit::"))
        if amount<1:
            print( "minimun deposit amount is 1!!")
        else:
            self.balance+= amount
            print(f'{amount} has been deposited in the account of {self.user_name},\n the current balance is {self.balance}  ')
details=[]
ask=input('enter your username and balance seperated by a comma:')
split=ask.split(",")
user_name=split[0].strip()
balance=int(split[1].strip())
detail=[user_name,balance]
details.append(detail)
account=bankaccount(user_name,balance)

while True:
    act=input("what do you want to do among :\ndeposit\nwithdrawl\ncheck balance ----")
    if act=="deposit":
        account.deposit()
    elif act=="withdrawl":
        account.withdrawl()
    elif act=="check balance":
        account.check_balance()
    elif act=="quit":
        print("thank you")
        break







