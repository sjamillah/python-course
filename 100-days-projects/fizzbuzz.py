#!/usr/bin/python3
#Script to play the fizzbuzz game

print("Welcome to the FizzBuzz Game!")
target = 100
for num in range(1, target + 1):
  if (num % 3 == 0) and (num % 5 == 0):
    print("FizzBuzz")
  elif num % 5 == 0:
    print("Buzz")
  elif num % 3 == 0:
    print("Fizz")
  else:
    print(num)
