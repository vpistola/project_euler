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
from itertools import count

#prime_list = utils.sieve(10000)

def compute():
    consecutives = []
    i = 0
    for n in count(647):
        i += 1
        #l = []
        #l = prime_factors(n)
        if len(prime_factors(n)) == 4: consecutives.append(n)  
        if i == 4 and len(consecutives) == 4:
            break
        elif i == 4 and len(consecutives) < 4:
            i = 0
            consecutives = []
        else:
            continue
    return consecutives
    
def prime_factors(n):
    i = 2
    factors = set()
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.add(i)
    if n > 1:
        factors.add(n)
    return factors

if __name__ == "__main__":
    t1 = time.time()
    print(compute())
    #print(prime_factors(134043))
    t2 = time.time()
    print("Time elapsed:", t2 - t1, "seconds")
    
    
# END