# MIDPOINT KAREL

As an exercise in solving algorithmic problems, you will program to find the midpoint of 1st Street. Say Karel starts in the 5x5 world. Karel should end in the center of 1st row facing East.

Before:

![image](https://github.com/user-attachments/assets/b08db4ab-be75-4dfb-aa50-54c235f1cb12)

After:

![image](https://github.com/user-attachments/assets/c7fbd776-3866-4eda-892c-53dd15f7264b)


Note that the final configuration of the world should have only a single beeper at the midpoint of the 1st row. Along the way, Karel is allowed to place additional beepers wherever it wants to, but must pick them all up again before it finishes. Similarly, if Karel paints/colors any of the corners in the world, they must all be uncolored before Karel finishes.

In solving this problem, you may count on the following facts about the world:

    1. Karel starts at bottom left corner of the world, facing east.

    2. The initial state of the world includes no interior walls or beepers.

    3. The world need not be square, but you may assume that it is at least as tall as it is wide.

If the width of the world is odd, Karel must put the beeper in the center square. If the width is even, Karel must drop a beeper on the left most of the two squares.
There are many different algorithms you can use to solve this problem so feel free to be creative!
You should design your program to run successfully in all possible worlds.
