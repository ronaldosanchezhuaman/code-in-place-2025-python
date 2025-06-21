from karel.stanfordkarel import *

def main():
    move2()
    pick_beeper()
    move()
    turn_left()
    move2()
    put_beeper()
    turn_left2()
    move2()
    turn_right()
    move3()
    turn_left2()

def turn_left2():
    turn_left()
    turn_left()

def turn_right():
    turn_left()
    turn_left()
    turn_left()

def move2():
    move()
    move()

def move3():
    move()
    move()
    move()
    
# There is no need to edit code beyond this point
if __name__ == '__main__':
    main()