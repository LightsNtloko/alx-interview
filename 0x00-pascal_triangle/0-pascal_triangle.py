#!/usr/bin/python3
"""
This module defines a function to generate Pascal's triangle.
"""


def pascal_triangle(n):
    """
    Generate Pascal's triangle of size n.

    Args:
        n (int): The size of Pascal's triangle.

    Returns:
        list: A list of lists of integers representing Pascal's triangle.
    """
    if n <= 0:
        return []

    triangle = [[1]]  # Initialize the first row

    for i in range(1, n):
        row = [1]  # Start each row with 1
        prev_row = triangle[i - 1]

        # Generate current row, summing adjacent elements from the previous row
        for j in range(1, i):
            row.append(prev_row[j - 1] + prev_row[j])

        row.append(1)  # End each row with 1
        triangle.append(row)

    return triangle
