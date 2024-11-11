This module solves the N Queens problem using a backtracking algorithm.
The N Queens problem involves placing N non-attacking queens on an N×N chessboard.
This script accepts a single command-line argument, N, representing the board's size
and the number of queens to place.

Usage:
./0-nqueens.py N

Where:
- N must be an integer greater than or equal to 4.
- The script outputs each solution as a list of queen positions for the N×N board.
- Each solution is formatted as a list of lists, where each sublist contains the row and column index of a queen.

Example:
./0-nqueens.py 4
Output:
[[0, 1], [1, 3], [2, 0], [3, 2]]
[[0, 2], [1, 0], [2, 3], [3, 1]]

The script will exit with an error message if:
- The incorrect number of arguments is provided.
- N is not an integer.
- N is less than 4.

Only the sys module is imported for command-line argument handling.
