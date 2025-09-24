studentDictionary = {
    'Elliott': 0,
    'Ryan': 0,
    'Alex': 0,
    'Grace': 0
}
for student in studentDictionary:
    print(student)
    floatStudentScore = float(input("What is your score?"))
    studentDictionary[student] = floatStudentScore
    print(studentDictionary)
    print("Iteration complete")
    
