#!/usr/bin/python3
#The projects tests the compatibility between two people using the names
print("Tests the compatibility between two people")
print("------------------------------------------")
name1 = input("Enter the names of the first person: ")
name2 = input("Enter the names of the second person: ")

#Checks the number of times the words "true" and "love" appear in the names of the two people
combined_names = name1 + name2
lower_names = combined_names.lower()
t = lower_names.count("t")
r = lower_names.count("r")
u = lower_names.count("u")
e = lower_names.count("e")
first_digit = t + r + u + e

l = lower_names.count("l")
o = lower_names.count("o")
v = lower_names.count("v")
e = lower_names.count("e")
second_digit = l + o + v + e

#Combines the two digits
score = int(str(first_digit) + str(second_digit))

#Tests the compatibility
if score < 10 or score > 90:
  print(f"Your score is {score}, you go together like coke and mentos.")
elif score >= 40 and score <= 50:
  print(f"Your score is {score}, you are alright together.")
else:
  print(f"Your score is {score}.")
