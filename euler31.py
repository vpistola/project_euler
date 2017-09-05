'''
Project Euler 31: Investigating combinations of English currency denominations

In England the currency is made up of pound, £, and pence, p, and there are eight coins in general circulation:

    1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) and £2 (200p).

It is possible to make £2 in the following way:

    1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p

How many different ways can £2 be made using any number of coins?

The problem sill be solved using the dynamic programming method.
Dynamic programming (also known as dynamic optimization) is a method for solving a complex problem by breaking it down into a collection of simpler subproblems, solving each of those subproblems just once, and storing their solutions.
A dynamic programming algorithm will examine the previously solved subproblems and will combine their solutions to give the best solution for the given problem.
'''

def compute():
    AMOUNT = 200
    combinations = [1] + [0] * AMOUNT
    for coin in [1, 2, 5, 10, 20, 50, 100, 200]:
        for i in range(len(combinations) - coin):
            combinations[i + coin] += combinations[i]
    return str(combinations[-1])


if __name__ == "__main__":
    print(compute())