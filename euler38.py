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
