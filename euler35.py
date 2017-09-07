'''
Problem 35: Circular Primes

The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.

There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

How many circular primes are there below one million?
'''

import time, utils

def compute():
    prime_list = utils.prime_list_up_to_n(999999)
    def circular_prime(n):
        s = str(n)
        return all( prime_list[int(s[i:] + s[:i])] for i in range(len(s)) )
    
    ans = sum(1 for i in range(len(prime_list)) if circular_prime(i))
    return str(ans)


if __name__ == "__main__":
    t1 = time.time()
    print(compute())
    t2 = time.time()
    print("Time elapsed:", t2 - t1, "seconds")
