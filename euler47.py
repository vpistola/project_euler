'''
Problem 47: Distinct primes factors

The first two consecutive numbers to have two distinct prime factors are:

14 = 2 × 7
15 = 3 × 5

The first three consecutive numbers to have three distinct prime factors are:

644 = 2² × 7 × 23
645 = 3 × 5 × 43
646 = 2 × 17 × 19.

Find the first four consecutive integers to have four distinct prime factors each. What is the first of these numbers?
'''

import time, utils
from functools import reduce
from collections import defaultdict

#prime_list = utils.sieve(1000000)

def compute():
    #D = defaultdict(list)
    #for n in range(1000000):
    #   D[n] = utils.divisors(n)
    pass
    
def prime_factors(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors

_primes = [2]

def factors(n):    
    return set(reduce(list.__add__, 
                ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))

if __name__ == "__main__":
    t1 = time.time()
    print(factors(646))
    t2 = time.time()
    print("Time elapsed:", t2 - t1, "seconds")
    
    
# QED