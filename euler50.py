'''
Problem 50: Consecutive prime sum

The prime 41, can be written as the sum of six consecutive primes:
	
	41 = 2 + 3 + 5 + 7 + 11 + 13

This is the longest sum of consecutive primes that adds to a prime below one-hundred.

The longest sum of consecutive primes below one-thousand that adds to a prime, contains 21 terms, and is equal to 953.

Which prime, below one-million, can be written as the sum of the most consecutive primes?
'''

import time, utils

prime_list = utils.upto(999999)
primes = utils.list_primes(999999)

def compute():
    ans = 0
    consecutive = 0
    for i in range(len(primes)):
        sum = primes[i]
        consec = 1
        for j in range(i + 1, len(primes)):
            sum += primes[j]
            consec += 1
            if sum >= len(prime_list):
                break
            if prime_list[sum] and consec > consecutive:
                ans = sum
                consecutive = consec
    return str(ans)
    
# This function gives another result = 535. The true prime number which is the sum of 
# consecutives (2,3,5,7,...) prime numbers 
def compute2():
    ans = 0
    L = []
    for i in utils.eratosthenes():
        ans += i
        L.append(ans)
        if ans > 1000000: break
    for n in range(len(L)-1, 0, -1):
        if utils.is_prime(L[n]): return n
    return None

 
if __name__ == "__main__":
    t1 = time.time()
    print(compute2())
    t2 = time.time()
    print("Time elapsed:", t2 - t1, "seconds")
    

# END