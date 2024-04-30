Challenge script

Can you Escape this now ? The Same As challenge 4 just listen carfully now :You have to find the shortest path through a platform maze, each tile in the maze could be a trap and make an end to your journey. luckily you found a letter, flipped it over for a set of diagrams, that will help you navigate the upcoming platform maze.Check Drive and Provided images(.png);

Difficulty

MEDIUM

Given maze an n x m matrix representing the platform maze, and hint is the hint matrix (n/2 x m/2) containing the symbols in the middle of each grouping of four tiles.
When you reach the platform maze, pay attention to the symbol. As importantly, you also need to consider which direction each symbol is facing, For example:

"l" means that the group of four tiles is rotated by 90° to the left.
Your Task is :
First find all the skull platforms as shown in the picture above by putting "X" in the corresponding cell in the matrix maze.
Example :

- maze = [["T", "T", "T", "T", "T", "T"],
            ["T", "T", "T", "T", "T", "T"],
            ["T", "T", "T", "T", "T", "T"],
            ["T", "T", "T", "T", "T", "T"],
            ["T", "T", "T", "T", "T", "T"],
            ["T", "T", "T", "T", "T", "T"]]

- hint = [["2", "3,l", "1,l,l"],
            ["1,r", "2,r,r", "3"],
            ["1,l,l", "3", "2,r"]]

6 6
T T T T T T
T T T T T T
T T T T T T
T T T T T T
T T T T T T
T T T T T T
3 3
2 3,l 1,l,l
1,r 2,r,r 3
1,l,l 3 2,r

Where:

The first line is the number of rows n and columns m respectively of the maze matrix.
The next n lines contain:
m times the character "T" (which means tale).
The next line (n+1) is the number of rows n' = n/2 and columns m' = m/2 respectively of the hint matrix.
The next n' lines contain:
m' unlimited comma separated values.
The marked matrix would be:

X X X X X T
T T T X T T
T T T T T X
X T X X X X
X T T X T X
T T X X T X

Where:

Each line contains characters that are either "T" (Tale) or "X" (Marked tale)

Data types:
maze, hint: matrix of char

Constraints:

-The number of "l" or "r" in a signle group of four tiles isnt limmited and they may appear together at any order.
-mark the skull platforms by capital "X".

You will be given an input txt file for the Test .Provide Us the Script you wrote with the Output.txt you got.

You Solved IT? cant Wait For you for The Next One.