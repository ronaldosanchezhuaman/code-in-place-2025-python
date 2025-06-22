from karel.stanfordkarel import *

"""
File: main.py
--------------------
When you finish writing this file, Karel should have repaired 
each of the columns in the temple
"""

def main():
    
    for i in range(3):
        up_column()
        down_column()
        move_next_column()
    up_column()
    down_column()
    """
    build the columns in the temple of artemis
    """
def up_column():
    turn_left()
    build_column()

def down_column():
    turn_left()
    turn_left()
    for i in range (4):
        move()
    turn_left()

def move_next_column():
    for i in range (4):
        move()

def build_column():
    while front_is_clear():
        put_beeper()
        move()
    put_beeper()

if __name__ == '__main__':
    main()