# Writing to a file
with open("students.txt", "w") as file:
    file.write("Anup - Pass\n")
    file.write("Raj - Pass\n")
    file.write("Sita - Fail\n")

print("File created successfully")
# Reading from a file
with open("students.txt", "r") as file:
    content = file.read()

print(content)