#!/usr/bin/python3
#Script to calculate max score without use of max function

print("calculates the highest score")
student_scores = input("Please input the student scores as integers: \n")
new_student_scores = student_scores.split()
for n in range(0, len(new_student_scores)):
  new_student_scores[n] = int(new_student_scores[n])
max_score = 0
for score in new_student_scores:
  if score > max_score:
    max_score = score
print(f"The student score is: {new_student_scores}")
print(f"The highest score in the class is: {max_score}")
