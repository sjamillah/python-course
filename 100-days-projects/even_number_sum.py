#!/usr/bin/python3
#Script to add even numbers in a set range

print("Adds all the even numbers from 0 to 1000")
target = int(input("Please input numbers from 0 to 1000: "))
total = 0
for num in range(1, target):
  if num % 2 == 0:
    total += num
    total_num = total + target
print(f"The total is: {total_num}")

#or

# second option
# print("Adds all the even numbers from 0 to 1000")
# target = int(input("Please input numbers from 0 to 1000: "))
# total = 0
# for num in range(2, target + 1, 2):
    # total += num
# print(f"The total is: {total}")
