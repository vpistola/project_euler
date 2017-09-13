'''
Problem 48: Self Powers

The series, 1**1 + 2**2 + 3**3 + ... + 10**10 = 10405071317.
Find the last ten digits of the series, 1**1 + 2**2 + 3**3 + ... + 1000**1000.
'''

import time

def compute():
    ans = 0
    for i in range(1, 1001):
        ans += i**i 
    return str(ans)[-10:]


if __name__ == "__main__":
    t1 = time.time()
    print(compute())
    t2 = time.time()
    print("Time elapsed:", t2 - t1, "seconds")
