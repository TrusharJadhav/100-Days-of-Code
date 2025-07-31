student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}

student_grades ={}
for key in student_scores:
    score=student_scores[key]
    if score>90:
        Grade="Outstanding"
    elif score>80:
        Grade="Exceeds Expectations"
    elif score>70:
        Grade="Acceptable"
    else:
        Grade="Fail"
    student_grades[key]=Grade
print(student_grades)