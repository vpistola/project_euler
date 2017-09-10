'''
Project Euler 40: Finding the nth digit of the fractional part of the irrational number

An irrational decimal fraction is created by concatenating the positive integers:

	0.123456789101112131415161718192021…

It can be seen that the 12th digit of the fractional part is 1.

If dn represents the nth digit of the fractional part, find the value of the following expression.

	d1 x d10 x d100 x d1000 x d10000 x d100000 x d1000000
'''

import time

def compute():
    s = ''.join(str(i) for i in range(1, 1000000))  
    ans = 1
    for n in range(7):
        ans *= int(s[10**n - 1])
    return str(ans)
    

if __name__ == "__main__":
    t1 = time.time()
    print(compute())
    t2 = time.time()
    print("Time elapsed:", t2 - t1, "seconds")