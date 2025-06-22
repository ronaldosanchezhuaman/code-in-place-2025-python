from karel.stanfordkarel import *

"""
Karel should fill the whole world with beepers.
"""


def main():
    
    while left_is_clear():
        move_to_wall_type_1()
        turn_left()
        move()
        face_east()
        if left_is_clear():
            move_to_wall_type_2()
            turn_left()
            move()
            face_east()
    move_south()
    if beepers_present():
        move_north()
        face_east()
        move_to_wall_type_2()
    else:
        move_north()
        face_east()
        move_to_wall_type_1()
    
    return_home()
    
def return_home():
    face_south()
    while front_is_clear():
        move()
    face_east()

def move_north():
    face_north()
    move()

def move_south():
    face_south()
    move()

def move_to_wall_type_1():
    put_beeper()
    if front_is_clear():
        move()
    while front_is_clear():
        move()
        put_beeper()
        if front_is_clear():
            move()
    return_oposite_wall()
    face_east()

def move_to_wall_type_2():
    if front_is_clear():
        move()
        move_to_wall_type_1()

def return_oposite_wall():
    turn_around()
    while front_is_clear():
        move()

def turn_around():
    turn_left()
    turn_left()    

def turn_right():
    for i in range(3):
        turn_left()

def face_south():
    while not_facing_south():
        turn_left()
def face_north():
    while not_facing_north():
        turn_left()
def face_east():
    while not_facing_east():
        turn_left()
def face_west():
    while not_facing_west():
        turn_left()
     

# There is no need to edit code beyond this point
if __name__ == '__main__':
    main()