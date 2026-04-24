students={
    "Anup":{"age":14, "grade":9, "score":85},
    "Raj": {"age": 15, "grade": 10, "score": 92},
    "Sita": {"age": 14, "grade": 9, "score": 78}
}

for name, info in students.items():

    if info['score']<=79:
        print(f"{name} -fail")
    else:
        print(f"{name} -pass")
        
    




