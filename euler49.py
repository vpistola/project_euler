'''
Problem 49: Prime Permutations

The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases by 3330, is unusual in two ways: 
	
    (i) each of the three terms are prime, and, 
	(ii) each of the 4-digit numbers are permutations of one another.

There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes, exhibiting this property, but there is one other 4-digit increasing sequence.

What 12-digit number do you form by concatenating the three terms in this sequence?
'''

import time, utils, itertools

cat=''.join
prime_list = utils.prime_list_up_to_n(10000)

def compute():
    L = []
    for n in range(1000, 10000):
        x = n + 3330
        y = n + 6660
        if y < 10000:
            if prime_list[n] and prime_list[x] and prime_list[y]:
                if has_same_digits(n, x, y): L.append((n, x, y))
    return str(L[1][0]) + str(L[1][1]) + str(L[1][2])
    
    
def has_same_digits(x, y, z):
	return sorted(str(x)) == sorted(str(y)) == sorted(str(z))
    

if __name__ == "__main__":
    t1 = time.time()
    print(compute())
    #print(prime_list[9629])
    t2 = time.time()
    print("Time elapsed:", t2 - t1, "seconds")
    
    
# END