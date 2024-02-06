#!/usr/bin/python3
#Script to play rock, paper, scissors with the computer
import random
choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))
Rock = '''    
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''
Paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''
Scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
images = [Rock, Paper, Scissors]
print(images[choice]) #prints the images based on your choice btn 0,1,2
computer_chose = random.randint(0, 2) #computer chooses a random number in the range
print(f"Computer chose: {images[computer_chose]}") #prints the image based on the computer choice
if computer_chose < choice:
  print("You win")
elif computer_chose > choice:
  print("You lose")
else:
  print("Play again")
