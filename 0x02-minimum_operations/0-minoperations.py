#!/usr/bin/python3
"""
Module 0-minoperations
Contains the function minOperations that calculates
the fewest number of operations needed to reach exactly n 'H' characters
"""


def minOperations(n):
    """
    Calculates the minimum number of operations required to reach
    exactly n 'H' characters in the file.

    The two operations allowed are 'Copy All' and 'Paste'. This function
    finds the fewest number of operations to achieve the target number
    of 'H' characters.

    Args:
        n (int): The target number of 'H' characters.

    Returns:
        int: The minimum number of operations needed to reach n 'H'
             characters, or 0 if n is impossible to achieve (i.e., n <= 1).
    """
    
    # Check if the input is an integer and greater than 1
    if not isinstance(n, int) or n <= 1:
        # If n is less than or equal to 1, or if n is not an integer,
        # it's impossible to achieve n 'H' characters
        return 0
    
    operations = 0  # Initialize the number of operations
    divisor = 2     # Start checking divisors from 2
    
    # Factorize n by dividing it by its smallest prime factors
    while n > 1:
        # While n is divisible by the current divisor
        while n % divisor == 0:
            # Add the divisor to the operations count
            operations += divisor
            # Update n by dividing it by the divisor
            n //= divisor
        # Move to the next possible divisor
        divisor += 1
    
    # Return the total number of operations needed
    return operations
