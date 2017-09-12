'''
Problem 46: Goldbach's other conjecture

It was proposed by Christian Goldbach that every odd composite number can be written as the sum of a prime and twice a square.

9 = 7 + 2 * 1**2
15 = 7 + 2 * 2**2
21 = 3 + 2 * 3**2
25 = 7 + 2 * 3**2
27 = 19 + 2 * 2**2
33 = 31 + 2 * 1**2

It turns out that the conjecture was false.

What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?
'''

import time, utils
from itertools import product
    
def main():
    primes = utils.sieve(10000)
    composites = set(n for n in range(2, 10000) if n not in primes)
    twicesquares = set(2*(n**2) for n in range(100))
    sums = set(sum(c) for c in product(primes, twicesquares))
    print(min(n for n in composites if n not in sums and n % 2 != 0))
    
if __name__ == "__main__":
    t1 = time.time()
    main()
    t2 = time.time()
    print("Time elapsed:", t2 - t1, "seconds")