turns=0


import random
a= random.randint(1,100)

while True:

    turns+=1

    try:
       guess=int(input("enter a number of your choice::"))
    except ValueError:
        print("invalid syntax")
    
    if guess==a:
        print(f"Your guess is exactly correct!! \n you got it right in {turns} turns")
        break
    elif guess> a:
        print("your guess is higher!!")
    elif guess < a:
        print("your guess is lower!!")
   