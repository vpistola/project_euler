'''
Problem 36: Double-base palindromes

The decimal number, 585 = 1001001001 (binary), is palindromic in both bases.
Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.
(Please note that the palindromic number, in either base, may not include leading zeros.)
'''

import time

def compute():
    ans = sum(i for i in range(1000000) if palindromic_both_bases(i))
    return str(ans)
    
    
def palindromic_both_bases(n):
    b = bin(n)
    s = str(n)
    if b[2:] == b[:1:-1] and s[:] == s[::-1]:
        return True
    return False
    
    
if __name__ == "__main__":
    t1 = time.time()
    print(compute())
    t2 = time.time()
    print("Time elapsed:", t2 - t1, "seconds")
