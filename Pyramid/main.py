from graphics import Canvas
import random

CANVAS_WIDTH = 600      # Width of drawing canvas in pixels
CANVAS_HEIGHT = 300     # Height of drawing canvas in pixels

BRICK_WIDTH	= 30        # The width of each brick in pixels
BRICK_HEIGHT = 12       # The height of each brick in pixels
BRICKS_IN_BASE = 14     # The number of bricks in the base

def main():
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    # TODO, your code here

    for row in range(BRICKS_IN_BASE):
        media=(6+row)*30/2
        bricks_for_row= BRICKS_IN_BASE-row

        for i in range(bricks_for_row):           
            x=media+i*BRICK_WIDTH
            #y=300-BRICK_HEIGHT-BRICK_HEIGHT*row
            y=CANVAS_HEIGHT-BRICK_HEIGHT-BRICK_HEIGHT*row
            x_end=x+BRICK_WIDTH
            y_end=CANVAS_HEIGHT-BRICK_HEIGHT*row
            canvas.create_rectangle(x, y,x_end, y_end,"yellow", "black")
    
if __name__ == '__main__':
    main()