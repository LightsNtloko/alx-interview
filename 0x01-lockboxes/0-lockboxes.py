#!/usr/bin/python3
"""
0-lockboxes.py
A module that defines the canUnlockAll function to check if all boxes can
be unlocked.
"""


def canUnlockAll(boxes):
    """
    Determines if all boxes can be unlocked.

    Args:
        boxes (list): A list of lists where each sublist represents keys
        in a box.

    Returns:
        bool: True if all boxes can be opened, False otherwise.
    """
    n = len(boxes)  # Total number of boxes
    opened_boxes = set([0])  # Start with the first box opened
    stack = [0]  # Start the stack with the first box

    while stack:
        box = stack.pop()  # Get the current box
        for key in boxes[box]:
            if key not in opened_boxes and key < n:
                opened_boxes.add(key)  # Mark the box as opened
                stack.append(key)  # Add the box to explore its keys

    return len(opened_boxes) == n  # Return True if all boxes are opened
