''' 
Project Euler 30: Find the sum of all the numbers that can be written as the sum of fifth powers of their digits

We need an upper bound if we don’t want to continue in eternity. So finding the upper bound is the secret to solving this problem. We need to find a number x*95 which gives us an x digit number. We can do this by hand. Since 95 = 59049, we need at least 5 digits. 5*95 = 295245, so with 5 digits we can make a 6 digit number. 6*95 = 354294. So 355000 seems like a reasonable upper bound to use.
'''

import time

def compute():
    L = []
    for i in range(1, 355000):
        ans = 0
        for num in str(i):
            ans += int(num) ** 5
        if i == ans: L.append(i)
    return sum(L)
    
if __name__ == "__main__":
    t1 = time.time()
    print(compute())
    t2 = time.time()
    print("Time elaplsed: ", t2 - t1, "seconds")