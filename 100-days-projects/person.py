#!/usr/bin/python3
#Script to pick a random person to pay the bill
import random
message = print("Picking a random person to pay the bill")
names_string = input("Give me a list of individual names separated by a comma with a space after the comma.")

#changes the names_string to a list using split method
names = names_string.split(", ")
print(names) #prints the list of the names
num_items = len(names) #checks the length of the names list

#picks a random number from the length of the names list
random_name = random.randint(0, num_items - 1)

#it shows the name of the person at the random number picked from the nameslist
person_to_pay = names[random_name]
print(f"The person to pay the bill is: {person_to_pay}")
