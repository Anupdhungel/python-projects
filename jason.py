import json
person={
    "Name":"Anup",
    "age":14,
    "skills":["python","problem solving"]

}

with open("person.json","w") as file:
    json.dump(person,file)

print("saved successfully!")

with open("person.json","r") as file:
    data = json.load(file)

print(data["Name"])
print(data["skills"])