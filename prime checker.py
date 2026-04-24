while True:
    num=int(input("enter the number of your choice"))
    
    

    if num>1:
        for i in range(2,num):
            if num % i ==0:
                print("the number is not prime")
                break
    else:
        print("the number is not prime")            