import math

# 9! = 362880
# 2 * 9! = 725760

# precond: 1 <= d <= 10
# we are given the digits 0, ..., d-1
# return the nth lexicographic permutation of the digits
def lexiperm(d: int, n: int):
    assert(n <= math.factorial(d))
    # hi -> highest modified digit
    hi = 0
    while (math.factorial(hi + 1) < n):
        h += 1
