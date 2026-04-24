
students = {
    "ram": {"age": 14, "score": 80},
    "shyam": {"age": 13, "score": 70},
    "kalyan": {"age": 12, "score": 90}
}

with open("results.txt", "w") as file:
    for name, info in students.items():
        if info["score"] < 80:
            file.write(f"{name} | Age: {info['age']} | Score: {info['score']} | Fail\n")
        else:
            file.write(f"{name} | Age: {info['age']} | Score: {info['score']} | Pass\n")

with open("results.txt","r") as file:
    content=file.read()
    print(content)