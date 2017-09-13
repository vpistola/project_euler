# utilities for the project euler
import itertools
from functools import reduce

million  = 10 ** 6      # 1,000,000
Ø        = frozenset()  # Empty set
distinct = set          # Function to return the distinct elements of a collection of hashables
identity = lambda x: x  # The function that returns the argument
cat      = ''.join      # Concatenate strings

def divisors(n): return list(i for i in range(1, n//2+1) if n%i == 0)

def eratosthenes():
    D = {}
    yield 2
    for q in itertools.islice(itertools.count(3), 0, None, 2):
        p = D.pop(q, None)
        if p is None:
            D[q*q] = q
            yield q
        else:
            x = p + q
            while x in D or not (x&1):
                x += p
            D[x] = p
    
def is_prime(x):
	if x <= 1:
		return False
	elif x <= 3:
		return True
	elif x % 2 == 0:
		return False
	else:
		for i in range(3, sqrt(x) + 1, 2):
			if x % i == 0:
				return False
		return True
    
def isqrt(n):
    "Integer square root (rounds down)."
    return int(n ** 0.5)
       
def sqrt(x):
	assert x >= 0
	i = 1
	while i * i <= x:
		i *= 2
	y = 0
	while i > 0:
		if (y + i)**2 <= x:
			y += i
		i //= 2
	return y   

# prime list generator    
def prime_list_up_to_n(n):
	result = [True] * (n + 1)
	result[0] = result[1] = False
	for i in range(sqrt(n) + 1):
		if result[i]:
			for j in range(i * i, len(result), i):
				result[j] = False
	return result
        
# prime list generator - alternative solution (slow for large n)
def sieve(n):
    numbers = list(range(2, n+1))
    p = 2
    j = 0
    done = False
    while not done:
        for i, n in enumerate(numbers):
            if n % p == 0 and n!=p:
                numbers.pop(i)
        j += 1
        p = numbers[j]
        if p**2 > n:
            done = True
    return numbers
   
# Return a list of the numbers in the prime factorization of n.   
def prime_factors(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors
    
def factors(n):    
    return set(reduce(list.__add__, 
                ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))
 
class Memoize:
    def __init__(self, f):
        self.f = f
        self.memo = {}
    def __call__(self, *args):
        if not args in self.memo:
            self.memo[args] = self.f(*args)
        return self.memo[args]
    
   
# end    