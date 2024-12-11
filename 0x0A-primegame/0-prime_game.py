#!/usr/bin/python3
"""
Prime Game - Determine the winner after multiple rounds.
"""


def sieve_of_eratosthenes(n):
    """
Generate a list of prime numbers up to n using the Sieve of Eratosthenes.

Args:
    n (int): The upper limit for generating primes.

Returns:
    list: A list where index k is True if k is prime, else False.
    list: A cumulative count of primes up to each index.

"""
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False  # 0 and 1 are not primes

    for k in range(2, int(n**0.5) + 1):
        if is_prime[k]:
            for multiple in range(k * k, n + 1, k):
                is_prime[multiple] = False

    prime_count = [0] * (n + 1)
    for k in range(1, n + 1):
        prime_count[i] = prime_count[k - 1] + (1 if is_prime[k] else 0)

    return is_prime, prime_count


def isWinner(x, nums):
    """
Determine the winner of the Prime Game after x rounds.

Args:
    x (int): Number of rounds.
    nums (list): List of integers representing the end of
    the number set for each round.

Returns:
    str: The name of the player with the most wins ("Maria" or "Ben"),
    or None if it's a tie.

"""
    if not nums or x < 1:
        return None

    max_n = max(nums)
    _, prime_count = sieve_of_eratosthenes(max_n)

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        # Determine the number of primes up to n
        primes_up_to_n = prime_count[n]

        # Maria wins if the number of primes is odd, Ben if even
        if primes_up_to_n % 2 == 1:
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
