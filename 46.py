import math

from my_module import is_prime

# return list of odd composite numbers up to n
def odds(n):
    res = []
    for i in range(9, n, 2):
        if not is_prime(i):
            res.append(i)
    return res

odds = odds(10000)
for x in odds:
    goldbach = False
    s = math.floor(math.sqrt(x / 2))
    while (s > 0):
        r = x - (2 * (s**2))
        if is_prime(r):
            goldbach = True
            break
        s -= 1
    if not goldbach:
        print(x)
        break
print('done')


