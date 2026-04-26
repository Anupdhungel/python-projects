print("Welcome to our travel agency!!")
user_name1=input("please enter your name:")
user_name=user_name1.capitalize()
cost_of_accomodation=int(input("enter the cost of accomodation per day:"))
period_of_travelling=int(input("enter the todal days travelled"))
cost_of_travelling=int(input("enter the total cost of travelling throught the trip\n[flights included]:"))
cost_of_other_activities=int(input("enter the total price spent in otheer activities\n[if not, enter 0]"))
total_cost_accomodation=cost_of_accomodation*period_of_travelling
total_amount=total_cost_accomodation+cost_of_travelling+cost_of_other_activities


print(user_name,"the total cost to be paid is Rs.",total_amount)
