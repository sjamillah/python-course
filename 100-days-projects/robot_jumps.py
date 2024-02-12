#!/usr/bin/python3
#script to make a robot make hurdle jumps

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

for x in range(6):
    move()
    jump()
    turn_left()
