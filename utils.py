# utilities for the project euler

#def is_prime(n):
#    if n==2 or n==3: 
#        return True
#    if n%2==0 or n<2: 
#        return False
#    for i in range(3,int(n**0.5)+1,2):   # only odd numbers
#        if n%i==0:
#            return False    
#    return True
    
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