# utilities for the project euler
import itertools

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
    
def is_prime(n):
    return all(n % i != 0 for i in range(2, n))
    
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
    
    
def prime_list_up_to_n(n):
	result = [True] * (n + 1)
	result[0] = result[1] = False
	for i in range(sqrt(n) + 1):
		if result[i]:
			for j in range(i * i, len(result), i):
				result[j] = False
	return result
    

class Memoize:
    def __init__(self, f):
        self.f = f
        self.memo = {}
    def __call__(self, *args):
        if not args in self.memo:
            self.memo[args] = self.f(*args)
        return self.memo[args]
    

    
# end    