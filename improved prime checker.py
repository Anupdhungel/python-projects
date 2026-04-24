
def prime(num):
    if num<=2:
        return False
    
    for i in range (2,num):
        if num % i== 0:
            return False
        else:
            return True
        

try :
    num2=input ("enter the number of your choice::")
    number=int(num2)
    if prime(number):
        print (f"{number} is a prime number")
    else:
        print(f"{number} is not a prime")

except ValueError:
    print("invalid syntax try again!!")

