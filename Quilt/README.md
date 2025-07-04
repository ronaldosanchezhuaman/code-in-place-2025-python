# QUILT
A quilt, as you may know, is a blanket often composed of repeating "patches". Here is a quilt in the real world:

![image](https://github.com/user-attachments/assets/53d439c4-37f5-4894-8625-5bc410c04049)

Your first objective is to recreate this quilt:

![image](https://github.com/user-attachments/assets/72711df3-f845-49f8-b997-6f3731a696ae)

Each patch has height and width of 100 pixels, given by the constant PATCH_SIZE. There are two different patch patterns that repeat in different locations.

In this assignment each patch will be defined by a function. For example consider the draw_square_patch function which is already implemented for you in the starter code:

    def draw_square_patch(canvas, start_x, start_y):
        # draws a purple frame at (start_x, start_y)
        ...



draw_square_patch is passed three parameters, 
<ol>
<li>canvas: the canvas upon which we are drawing</li>
<li>start_x: the left side of the patch is start_x pixels from the left side of the canvas</li>
<li>start_y: the top of the patch is start_y pixels from the top of the canvas</li>
</ol>

This function can be reused as many times as you like. For example main calls it with different values for start_x and start_y. Different style patches, like the circle patch will have their own functions, but will take in the same three parameters.

The starter code has two places marked TODO. Fill them in to solve the task. You will need to define the circle patch function and make all the necessary function calls in order to draw the second row.

    # TODO: your code here



<h1>Milestone 1: Circle Patch</h1>
The draw_circle_patch function has not been implemented. Your first task is to complete the code in the body of draw_circle_patch. You should simply draw a circle that fills the patch at the provided location. The color for the circle in this demonstration is 'salmon'. Once you have implemented this function, your quilt should look like this:

<h1>Milestone 2: Second Row</h1>
The main function currently creates four patches. Your next job is to add four more lines to main so that it draws the second row. Note that the start_y values should all be PATCH_SIZE because the second row is PATCH_SIZE pixels from the top of the canvas.

<h1>Milestone 3: Collaborate</h1>
When you are done, push the "Check Correct" button. Then, you can optionally participate in making a big and wonderful Code in Place quilt. Create the most interesting patch you can think of and share the function definition on the forum. Find patches you love and incorporate them into your quilt.

To keep everything standard, each patch function should all take the same three parameters (canvas, start_x, start_y). All patches should be designed and should all be 100 pixels wide by 100 pixels high.
