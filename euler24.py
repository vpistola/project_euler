from itertools import permutations, combinations, islice

def compute():
    ans = next(islice(sorted(permutations(range(10))), 999999, None), None)
    return str(ans)

if __name__ == '__main__':
    print(compute())