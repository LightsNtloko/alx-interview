#!/usr/bin/python3
"""
0-nqueens.py

This module solves the N Queens problem using a backtracking algorithm.
The N Queens problem involves placing N non-attacking queens on an N×N chessboard.
This script accepts a single command-line argument, N, representing the board's size
and the number of queens to place.

Usage:
    ./0-nqueens.py N

Where:
    - N must be an integer greater than or equal to 4.
    - The script outputs each solution as a list of queen positions for the N×N board.
    - Each solution is formatted as a list of lists, where each sublist contains
      the row and column index of a queen.

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
"""

import sys

def print_solution(solution):
    """Print a single solution in the required format."""
    print([[r, c] for r, c in enumerate(solution)])

def is_safe(solution, row, col):
    """
    Check if it's safe to place a queen at (row, col).

    A position is safe if there is no queen in the same column,
    and no queen in either of the two diagonals for the given row.
    """
    for r, c in enumerate(solution[:row]):
        if c == col or abs(c - col) == abs(r - row):
            return False
    return True

def solve_nqueens(n):
    """
    Use backtracking to find and print all solutions for N queens.

    This function initializes an empty board and uses recursion
    to explore all possible solutions by placing queens row by row.
    """
    def backtrack(row, solution):
        if row == n:
            print_solution(solution)
            return
        for col in range(n):
            if is_safe(solution, row, col):
                solution[row] = col
                backtrack(row + 1, solution)

    backtrack(0, [-1] * n)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    solve_nqueens(N)
