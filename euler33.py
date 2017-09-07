'''
Project Euler 33: Discover all the fractions with an unorthodox cancelling method

The fraction 49/98 is a curious fraction, as an inexperienced mathematician in attempting to simplify it may incorrectly believe that 49/98 = 4/8, which is correct, is obtained by cancelling the 9s.

We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

There are exactly four non-trivial examples of this type of fraction, less than one in value, and containing two digits in the numerator and denominator.

If the product of these four fractions is given in its lowest common terms, find the value of the denominator.
'''

import time, fractions

def compute():
    # The only equation that holds is: (10n + i)/(10i + d) = n/d => d(10n + i) = n(10i + d)
    den_prod = 1
    nom_prod = 1
    for i in range(1, 10):
        for den in range(1, i):
            for nom in range(1, den):
                if (den*(10*nom + i) == nom*(10*i + den)):
                    den_prod *= den
                    nom_prod *= nom
    return str(den_prod // fractions.gcd(nom_prod, den_prod))

if __name__ == "__main__":
    t1 = time.time()
    print(compute())
    t2 = time.time()
    print("Time elapsed:", t2 - t1, "seconds")