#!/usr/bin/python3
"""
This module provides a function to calculate the perimeter
of an island described in a grid.
"""


def island_perimeter(grid):
    """
    Calculates the perimeter of the island in the grid.

    Args:
        grid (list of list of int): A 2D grid representing water (0) and
        land (1).

    Returns:
        int: The perimeter of the island.
    """
    rows = len(grid)
    cols = len(grid[0])
    perimeter = 0

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:  # Land cell
                # Assume all four sides contribute to the perimeter
                perimeter += 4

                # Check the cell above
                if i > 0 and grid[i - 1][j] == 1:
                    perimeter -= 2  # Remove shared edge

                # Check the cell to the left
                if j > 0 and grid[i][j - 1] == 1:
                    perimeter -= 2  # Remove shared edge

    return perimeter
