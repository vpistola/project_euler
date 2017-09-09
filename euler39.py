'''
Problem 39: Integer right triangles

If p is the perimeter of a right angle triangle with integral length sides, {a,b,c}, there are exactly three solutions for p = 120.

{20,48,52}, {24,45,51}, {30,40,50}

For which value of p ≤ 1000, is the number of solutions maximised?
'''

#We are given two equations to work with
#
#    a2 + b2 = c2 (1)
#    a + b+ c = p (2)
#
#Thus we can rewrite (2) as c = p  – a – b and insert it into (1) yielding
#
#    a**2 + b**2 = (p-a-b)**2 = p**2 + a**2 + b**2 -2pa – 2pb + 2ab
#Isolating b on one side of that equation yields
#
#   b = (p**2 -2pa) / (2p-2a)
#
#So for all values of p and a where b is an integer is a Pythagorean triplet with the perimeter #p.
#
#We can further make a bit of analysis on (1)
#
#if a and b is even so is c and thus p is even
#
#if a or b (but not both) is odd then c is odd and thus p is even
#
#if both a and b is odd then c is even and thus p is even
#
#Therefore we only need to check the numbers where p is even.
#
#Furthermore we know a < c and b < c and without loss of generality we can assume that a ≤ b #(otherwise we could switch them) which gives us that a ≤ b < c.  That implies  a < p/3 and #thus we don’t need to check values higher than that.

import time

def compute():
    ans = 0
    ans_solutions = 0
    for p in range(2, 1001, 2):
        num_of_solutions = 0
        for a in range(2, p//3):
            if(p*(p - 2*a) % (2*(p-a)) == 0):
                num_of_solutions += 1
        if(num_of_solutions > ans_solutions):
            ans_solutions = num_of_solutions
            ans = p
    return str(ans)

if __name__ == "__main__":
    t1 = time.time()
    print("p = ", compute())
    t2 = time.time()
    print("Time elapsed:", t2 - t1, "seconds")