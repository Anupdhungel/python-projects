# Salary classifier
while True:
    employee_name = input("Enter employee name: ").capitalize()

    try:
     salary = int(input("Enter monthly salary: "))
    except ValueError:
     print("Invalid input. Please enter a number.")
     continue

    if salary <= 20000:
        print(f"{employee_name} has a low salary!")
    elif salary <= 50000:
        print(f"{employee_name} has a medium salary!")
    else:
        print(f"{employee_name} has a high salary!")

    annual_salary=salary*12
    print(f'annual salary:{annual_salary}')


    ask=input("Do you want to check salary of another employee::").capitalize()
    if  ask == "No":
        break
       