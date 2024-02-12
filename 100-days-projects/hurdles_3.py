#!/usr/bin/python3
#Script to make hurdle jumps of any type of hurdle jumps

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
        turn_left()

while at_goal() != True:
    if wall_in_front():
        jump()
    else:
        move()
