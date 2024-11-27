#!/usr/bin/python3
"""
This module is for solving the change problem
"""


def makeChange(coins, total):
    """
    Firstly determine the fewest number of coins needed to meet a
    given amount in total.

    Args:
        coins (list): This is a list of coin denominations available.
        total (int): This is the target amount to be achieved with the coins.

    Returns:
        int: This is the total number of coins needed.
             If total is 0 or less, return 0.
             If the total cannot be achieved, return -1.
    """

    if total <= 0:
        return 0

    # Initialize DP table with a large value (greater than any possible value)
    dp = [float('inf')] * (total + 1)
    dp[0] = 0

    for coin in coins:
        for k in range(coin, total + 1):
            dp[k] = min(dp[k], dp[k - coin] + 1)

    return dp[total] if dp[total] != float('inf') else -1
