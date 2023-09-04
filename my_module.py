'''Frequently used functions'''

import math

def is_prime(x: int) -> bool:
    if x < 2:
        return False
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True

def permutation(arr):
    if len(arr) < 2:
        return [arr]
    res = []
    for i in range(len(arr)):
       m = arr[i]
       remLst = arr[:i] + arr[i+1:]
       # Generating all permutations where m is first element
       for p in permutation(remLst):
           res.append([m] + p)
    return res
