#!/usr/bin/python3
"""
This module provides a function to determine the fewest number of coins
needed to meet a given total.
"""


def makeChange(coins, total):
    """
    Determines the fewest number of coins needed to meet the given total.

    Args:
        coins (list): List of the values of the coins in your possession.
        total (int): The target amount to achieve using the coins.

    Returns:
        int: Minimum number of coins needed to meet the total.
             Returns 0 if the total is 0 or less.
             Returns -1 if the total cannot be achieved with the given coins.
    """
    if total <= 0:
        return 0

    # Sort coins in descending order for the greedy algorithm
    coins.sort(reverse=True)

    count = 0
    for coin in coins:
        # Use as many coins of this denomination as possible
        count += total // coin
        total %= coin

        # If total becomes 0, we've successfully achieved the amount
        if total == 0:
            return count

    # If we cannot achieve the total, return -1
    return -1
