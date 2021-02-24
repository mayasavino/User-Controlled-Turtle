"""
A user-controlled turtle.

file: navigate.py
author: Maya Savino
date: 16 February 2021
assignment: Lab 3

"""

import turtle


"""Moves turtle left as many degrees as user says."""
def left(degrees):
    ut.left(degrees)

"""Moves turtle right as many degrees as user says."""
def right(degrees):
    ut.right(degrees)

"""Moves turtle forward as many steps as user says."""
def forward(steps):
    ut.forward(steps)
        

"""User Controls:"""
if __name__ == "__main__":
    turtle.shape("turtle")
    ut = turtle.Turtle()
    print("Hello and welcome to the interactable turtle.")
    print("Please use the following commands to direct her:")
    print("Left; Right; Forward; Stop")
    go = input("Where?: ")
    go = go.lower()

    while (go != "stop"):

        if (go == "left"):
            degrees = int(input("How many degrees?: "))
            movement = left(degrees)
            go = input("Where next?: ")
        
        elif (go == "right"):
            degrees = int(input("How many degrees?: "))
            movement = right(degrees)
            go = input("Where next?: ")

        elif (go == "forward"):
            steps = int(input("How many steps?: "))
            movement = forward(steps)
            go = input("Where next?: ")

    if (go == "stop"):
        print("You have arrived at your destination.")