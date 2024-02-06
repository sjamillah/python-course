#!/usr/bin/python3
#Script to mark a spot inorder to find a treasure
"""
Example Input 1
B3

Example Output 1
Hiding your treasure! X marks the spot.
['⬜️', '️⬜️', '️⬜️']
['⬜️', '⬜️', '️⬜️']
['⬜️️', 'X', '⬜️️']
"""
#intialization of lists
list1 = ["⬜️","⬜️","⬜️"]
list2 = ["⬜️","⬜️","⬜️"]
list3 = ["⬜️","⬜️","⬜️"]

#the nested list(3*3 matrix)
map = [list1, list2, list3]
print("Hiding your treasure! X marks the spot.")
message = input("Where do you want to put the treasure using the X spot?")
mark = message[0].lower() #sets the initial input character of message to lowercase
abc = ["a", "b", "c"] #user input characters for the index
letter_index = abc.index(mark) #the lowercase input of mark using the letters
number_index = int(message[1]) - 1 #deducts one from the first index to be 0
map[letter_index][number_index] = "X" #marks X to the specified spot ex: b3
print(f"{list1}\n{list2}\n{list3}")
