student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}
""" Scores 91 - 100: Grade = "Outstanding"

Scores 81 - 90: Grade = "Exceeds Expectations"

Scores 71 - 80: Grade = "Acceptable"

Scores 70 or lower: Grade = "Fail" """

student_grades = {}

for students in student_scores:
    
    score = student_scores[students]

    if   score > 90:
        student_grades[students] = "Outstanding"
    elif score > 80:
        student_grades[students] = "Exceeds Expectations"
    elif score > 70:
        student_grades[students] = "Acceptable"
    else:
        student_grades[students] = "Fail"


print(student_grades)
