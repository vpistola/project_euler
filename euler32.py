'''
Project Euler 32: Find the sum of all numbers that can be written as pandigital products

We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once; for example, the 5-digit number, 15234, is 1 through 5 pandigital.

The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing multiplicand, multiplier, and product is 1 through 9 pandigital.

Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.
'''

import time, utils

def compute():
	# For contradiction suppose a candidate (x, y, z) has z >= 10000.
	# Then x*y consumes at least 5 digits. With the 4 (or fewer) remaining digits, even the
	# upper bound of x=99 and y=99 produces a product of x*y < 10000, which is unequal to z.
	# Therefore we need the product z < 10000 to be able to find possible x and y values.
    ans = sum(i for i in range(1, 10000) if prod_is_pandigital(i))
    return str(ans)


def prod_is_pandigital(n):
    for d in utils.divisors(n):
        t = str(n) + str(d) + str(n // d)
        if ''.join(sorted(t)) == '123456789':
            return True
    return False        
    
    
if __name__ == "__main__":
    t1 = time.time()
    print(compute())
    t2 = time.time()
    print("Time elapsed: ", t2 - t1, "seconds")