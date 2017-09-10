'''
Problem 41: Pandigital Prime

We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital and is also prime.

What is the largest n-digit pandigital prime that exists?.

Analysis:
A number is divisible by 3 if and only if the sum of the digits of the number is divisible by 3. We can rather easily find the digit sum of pandigital numbers since we know the digits:

1+2+3+4+5+6+7+8+9 = 45
1+2+3+4+5+6+7+8 = 36
1+2+3+4+5+6+7 = 28
1+2+3+4+5+6 = 21
1+2+3+4+5 = 15
1+2+3+4 = 10
1+2+3 = 6
1+2 = 3

It is clear that all pandigital numbers except 4 and 7 digit ones are divisible by 3 and thus can’t be primes.  So the largest n-digit pandigital prime is 7654321. 
'''

import time

def compute():
    for i in range(9,0,-1):
        arr = list(range(i,0,-1))
        s = ''.join(str(x) for x in arr)
        if not int(s) % 3 == 0:
            return s


if __name__ == "__main__":
    t1 = time.time()
    print(compute())
    t2 = time.time()
    print("Time elapsed:", t2 - t1, "seconds")
    
    
# end