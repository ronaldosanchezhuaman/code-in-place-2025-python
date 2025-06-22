from karel.stanfordkarel import *

"""
Karel should fill the whole world with beepers.
"""

def main():
    """
    You should write your code to make Karel do its task in
    this function. Make sure to delete the 'pass' line before
    starting to write your own code. You should also delete this
    comment and replace it with a better, more descriptive one.
    """
    while left_is_clear():
        fill_row()
        step_column()
    move_to_corner()

def fill_row():
    move_to_corner()
    turn_around()
    return_row()

def move_to_corner():
    put_beeper()
    while front_is_clear():
        move()
        put_beeper()

def turn_around():
    turn_left()
    turn_left()

def return_row():
    while front_is_clear():
        move()

def step_column():
    turn_right()
    move()
    turn_right()
    
def turn_right():
    for i in range(3):
        turn_left()
# There is no need to edit code beyond this point
if __name__ == '__main__':
    main()