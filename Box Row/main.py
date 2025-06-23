from graphics import Canvas

CANVAS_WIDTH = 400
CANVAS_HEIGHT = 200
N_BOXES = 5
BOX_SIZE = CANVAS_WIDTH / N_BOXES

def main():
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)

    for i in range (N_BOXES):
        left_x=i*BOX_SIZE
        top_y=200-BOX_SIZE
        right_x=BOX_SIZE*i+BOX_SIZE
        bottom_y=200

        canvas.create_rectangle(
            left_x,
            top_y,
            right_x,
            bottom_y,
            "white",
            "black"
    )


# There is no need to edit code beyond this point

if __name__ == '__main__':
    main()