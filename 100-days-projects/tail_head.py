#!/usr/bin/python3
#script to pick by random tails or heads
import random
message = print("What is your choice? 0 or 1?")
choice = random.randint(0, 1)
if choice == 0:
    print("Tails")
else:
    print("Heads")
