from karel.stanfordkarel import *

"""
File: main.py
--------------------
When you finish writing this file, Karel should be able to find
the midpoint
"""

def main():
    """
    You should write your code to make Karel do its task in
    this function. Make sure to delete the 'pass' line before
    starting to write your own code. You should also delete this
    comment and replace it with a better, more descriptive one.
    """
    turn_left()
    while front_is_clear():
        move()
        if front_is_clear():
            move()
            turn_right()
            move()
            turn_left()
    
    turn_around()
    while front_is_clear():
        move()
    turn_left()
    put_beeper()

def turn_around():
    for i in range(2):
        turn_left()
def turn_right():
    for i in range(3):
        turn_left()

if __name__ == '__main__':
    main()