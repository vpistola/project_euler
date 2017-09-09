'''
Problem 38: Pandigital Multiples

Take the number 192 and multiply it by each of 1, 2, and 3:

    192 x 1 = 192
    192 x 2 = 384
    192 x 3 = 576

By concatenating each product we get the 1 to 9 pandigital, 192384576. We will call 192384576 the concatenated product of 192 and (1,2,3)

The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4, and 5, giving the pandigital, 918273645, which is the concatenated product of 9 and (1,2,3,4,5).

What is the largest 1 to 9 pandigital 9-digit number that can be formed as the concatenated product of an integer with (1,2, ... , n) where n > 1?
'''

#First of all the fixed number must contain less than 5 digits, since n has to be greater than 1.
#
#Second thing to not in our analysis is that we are given a candidate which starts with 9, so #the fixed number we need to find needs to start with 9 as well which gives us some properties #to use in the analysis.
#
#If the fixed number is 2 digit we wont be able to generate a 9 digit number since n = 3 yields #an 8 digit number and n=4 yields an 11 digit number. Same goes for 3 digit numbers where we #end at 7 or 11 digits in the result. That leaves us with a four digit number starting with 9.
#
#So already now we can limit the search to numbers between 9123 and 9876 a mere 753 numbers.
#
#We can rather easily limit it a bit more. If the second digit is >4 then we get a carry over #which results in the multiplying by 2 part will yield 19xxx instead of 18xxx and thus we have #two 9’s which are not possible solutions. Further more non of the digits can be 1 since we #will end up with a solution candidate with two 1’s in it.
#
#So the solution space can be shrunk to numbers between 9234 and 9487 which means we would need #to check 253 solutions.

import time

def compute():
    result = ''
    for i in range(9387, 9233, -1):
        result = str(i) + str(2*i)
        if ''.join(sorted(result)) == '123456789': break
    return result


if __name__ == "__main__":
    t1 = time.time()
    print(compute2())
    t2 = time.time()
    print("Time elapsed:", t2 - t1, "seconds")
