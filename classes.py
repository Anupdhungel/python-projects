class Student:
    def __init__(self, name, age, score):
        self.name=name
        self.age=age
        self.score=score

    def result(self):
        if self.score< 80:
            return "fail"
        else:
            return "pass"
        


students = []
for i in range(3):
    
    data = input(f"Enter details for student {i+1}: ")

    # split, create object, append to list
    split=data.split(",")
    name=split[0].strip()
    age=int(split[1].strip())
    score=int(split[2].strip())


    student=Student(name, age, score)
    students.append(student)
for student in students:
    print(f'{student.name}-{student.result()}')

with open("result.txt","w")as file:
    for student in students:
        file.write(f"{student.name}--{student.result()}\n")

with open("result.txt","r") as file:
    print(file.read())