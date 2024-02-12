#!/usr/bin/python3
#Script to make a robot do hurdle jumps using while loop

def turn_right():
    turn_left()
    turn_left()
    turn_left()

def jump():
        turn_left()
        move()
        turn_right()
        move()
        turn_right()
        move()

while at_goal() != True: #runs until the loop because true then it stops
    move()
    jump()
    turn_left()
