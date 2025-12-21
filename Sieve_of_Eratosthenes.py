"""
_HARD _ Sieve of Eratosthenes (about prime numbers)
_Let's say you need to display all the prime numbers from 2 to 10 billion (1010), 
because you want to impress your boss or something. 
To work out if a number is prime, 
you need to see if any of the prime numbers less than its square root divide it. 
So for numbers around 10 billion, 
we'd need to check every prime number up to about 100,000 to see if it's a divisor. 
But we don't want to waste our time recomputing all those prime numbers every single time we want to test a big number for primality. We want a list of primes up to 100,000, and the best (non-highly complicated) way to construct such a list is the Sieve of Eratosthenes (it's very likely that you don't know anywhere near enough maths to try the faster Quadratic Sieve. 
You can look it up on Wikipedia, or follow the guide below.
"""

import math 
LIMIT = 100

primality_list = [True] * (LIMIT + 1)
primality_list[0] = primality_list[1] = False

for biggest_prime_so_far in range(2, int(math.sqrt(LIMIT))+1):
    if primality_list[biggest_prime_so_far]:
        for multiple in range(biggest_prime_so_far**2, LIMIT+1, biggest_prime_so_far):
            primality_list[multiple] = False

primes = [index for index, is_prime in enumerate(primality_list) if is_prime]

def is_very_large_prime(n, prime_list):
    if n <= LIMIT:
        return primality_list[n]

        for p in prime_list:
            if p * p > n:
                break
            if n % p == 0:
                return False
        return n > 1

test_num = 2
if is_very_large_prime(test_num ,primes):
    print(f"{test_num} is prime!")
else:
    print(f"{test_num} is composite.")

print(primality_list)