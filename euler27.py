'''
Euler discovered the remarkable quadratic formula:

n**2+n+41

It turns out that the formula will produce 40 primes for the consecutive integer values 0≤n≤39
. However, when n=40,40**2+40+41=40(40+1)+41 is divisible by 41, and certainly when n=41,41**2+41+41

is clearly divisible by 41.

The incredible formula n**2−79n+1601
was discovered, which produces 80 primes for the consecutive values 0≤n≤79. The product of the coefficients, −79 and 1601, is −126479.

Considering quadratics of the form:
    n**2+an+b, where |a|<1000 and |b|≤1000

where |n|
is the modulus/absolute value of n
e.g. |11|=11 and |−4|=4

Find the product of the coefficients, a
and b, for the quadratic expression that produces the maximum number of primes for consecutive values of n, starting with n=0.
'''

import itertools, utils

prime_list = utils.prime_list_up_to_n(1000)

def compute():
    ans = []
    def f(n, a, b): return n*n + a*n + b
    for a in range(-999, 1000):
        for b in range(2, 1000):
            for n in itertools.count():
                ans1 = f(n,a,b)
                if ans1 > 0 and is_prime(ans1):
                    ans.append((a,b))
                return max(ans)    


def is_prime(n):
    if n < 0: return False
    elif n < len(prime_list): return prime_list[n]
    else: return utils.is_prime(n)

        
if __name__ == '__main__':
    print(compute())


# end