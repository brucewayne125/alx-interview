#!/usr/bin/python3
"""
Maria and Ben are playing a game. Given a set of consecutive integers starting
from 1 upto including n, they take turns choosing a prime number from the set
and removing that number and its multiples from the set.
The player that cannot make a move loses the game.
"""


def isWinner(x, nums):
    """
    Determines the winner of each game and returns the overall winner.
    Args:
        x (int): Number of rounds.
        nums (list): List of integers for each round.
    Returns:
        str: Name of the player with the most wins, or None if it's a tie."""
    if x < 1 or not nums:
        return None

    def eratosthenes(maximus):
        """
        Generate a list of primes upto maximus using the Sieve of Eratosthenes.
        """
        isPrime = [True] * (maximus + 1)
        isPrime[0] = isPrime[1] = False
        for i in range(2, int(maximus**0.5) + 1):
            if isPrime[i]:
                for j in range(i * i, maximus + 1, i):
                    isPrime[j] = False
        return isPrime
    maximus = max(nums)
    isPrime = eratosthenes(maximus)

    primeCount = [0] * (maximus + 1)
    for i in range(1, maximus + 1):
        primeCount[i] = primeCount[i - 1] + (1 if isPrime[i] else 0)

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        if primeCount[n] % 2 == 0:
            ben_wins += 1
        else:
            maria_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
