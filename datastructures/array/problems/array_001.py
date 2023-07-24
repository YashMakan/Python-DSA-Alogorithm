"""
Q: Program to print prime numbers from 1 to N.
Example:
    Input: N = 10
    Output: 2, 3, 5, 7
    
    Input: N = 5
    Output: 2, 3, 5

Prime number: A number ‘n’ is prime if it is not divisible by any number other than 1 and n. In other words a number is
              prime if it is not divisible by any number from 2 to n-1. so, we have to run a loop from 2 to n-1 and If
              a number is divisible by any number from 2 to n-1 it is not a prime number.
"""
import math


def is_prime_number(number: int) -> bool:
    if number < 2:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
    return True


def get_all_prime_numbers(n: int) -> list:
    primes: list = []
    for i in range(2, n + 1):
        if is_prime_number(i):
            primes.append(i)
    return primes


def get_all_prime_numbers_by_sieve_of_eratosthenes(n: int) -> list:
    primes: list = list(range(2, n))
    for i in range(2, int(math.sqrt(n)) + 1):
        if i in primes:
            for j in range(i * i, n, i):
                primes.remove(j)
    return primes


if __name__ == "__main__":
    N = 10
    arr: list = get_all_prime_numbers(N)
    # arr: list = get_all_prime_numbers_by_sieve_of_eratosthenes(N)
    print(arr)
