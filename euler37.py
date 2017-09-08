'''
Problem 37: Truncatable Primes

The number 3797 has an interesting property. Being prime itself, it is possible to continuously remove digits from left to right, and remain prime at each stage: 3797, 797, 97, and 7. Similarly we can work from right to left: 3797, 379, 37, and 3.

Find the sum of the only eleven primes that are both truncatable from left to right and right to left.

NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.
'''

import time, itertools
from utils import is_prime


# first version of the compute function
def compute():
    L = []
    for i in itertools.count(10):
        if truncatable(i): L.append(i)
        if len(L) == 11: break
    return str(sum(L))


# second version of the compute function
def compute2():
    ans = sum(itertools.islice(filter(truncatable, itertools.count(10)), 11))
    return str(ans)
    

# Finds out if the number is a truncatable prime (running time => 19 sec)    
def truncatable(n):
    if not is_prime(n): return False
    s = str(n)
    slen = len(s)
    for i in range(slen):
        if not is_prime(int(s[i:])): return False
        if not is_prime(int(s[:slen-i])): return False
    return True


if __name__ == "__main__":
    t1 = time.time()
    print(compute())
    t2 = time.time()
    print("Time elapsed:", t2 - t1, "seconds")
