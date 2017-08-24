from itertools import combinations

def divisors(n): return list(i for i in range(1, n//2+1) if n%i == 0)
    
def abundants():
    abundant_list = set()
    ans = 0
    for i in range(1, 28123):
        if sum(divisors(i)) > i:
            abundant_list.add(i)
    return abundant_list    #str(ans)

def sum_of_abundants():
    global abundants_nums
    l = set()
    for i in abundants_nums:
        for j in abundants_nums:
            if i+j < 28123:
                l.add(i+j)
    return l
    
abundants_nums = abundants()
abundants_sum = sum_of_abundants()
ans = set(range(28123)) - abundants_sum 
#print( ans )
#print( len(ans) ) 
print(sum(ans)) 