## Challenge script

With the knowledge you gained from localizing all the trap platforms within the maze of sherlock needs to get out, you set your sights on the next crucial objective: finding the largest connected subgraph among the remaining platforms.As you carefully examine the matrix representing the maze,

## Difficulty

HARD

you realize that the key lies in identifying the interconnected sections.
A connected subgraph consists of a subset of platforms that are directly connected to each other
through horizontal or vertical edges. By traversing these connected platforms, 
you can navigate the maze efficiently and bypass potential dangers.

Your task:
Given marked_maze which represent the output of the Platform Maze (Part 1) challenge.
Your task is to find the largest connected sub-graph in the maze.

Example:
Given this input:

6 6
X X X X X T
T T T X T T
T T T T T X
X T X X X X
X T T X T X
T T X X T X

Where:

First line represent n m, the number of rows and columns of the maze.
Next n lines contains m characters that are either "T" (Tile) or "X" (Marked tile).
The largest connected sub graph is:

16
0 5
1 5
1 4
2 4
2 3
2 2
1 2
1 1
1 0
2 0
2 1
3 1
4 1
4 2
5 1
5 0

Where:

The first line is the number n of nodes in the graph.
The next n lines containes the row index and column index respectively.

Data types:
marked_maze: matrix of char
Constraints
Notice that the row indexes are sorted asc and column indexes are sorted desc!

You will be provided input.txt and give the script and Output.txt .