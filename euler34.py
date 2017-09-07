'''
Project Euler 34: Find the sum of all numbers which are equal to the sum of the factorial of their digits

145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.
Find the sum of all numbers which are equal to the sum of the factorial of their digits.
Note: as 1! = 1 and 2! = 2 are not sums they are not included.
'''

import time, math

def compute():
    # As stated in the problem, 1 = 1! and 2 = 2! are excluded.
	# If a number has at least n >= 8 digits, then even if every digit is 9,
	# n * 9! is still less than the number (which is at least 10^n). 
    ans = sum(i for i in range(3, 10000000) if num_is_curious(i))
    return str(ans)


def num_is_curious(n):
    sum1 = 0
    for digit in str(n):
        sum1 += math.factorial(int(digit))
    if sum1 == n: return True 
    return False

if __name__ == "__main__":
    t1 = time.time()
    print(compute())
    t2 = time.time()
    print("Time elapsed:", t2 - t1, "seconds")