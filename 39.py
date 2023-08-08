# a + b + c = p
# a**2 + b**2 = c**2
# c is the longest side => c > p/3
# also a + b > c => c < p/2
# thus, only need to test p/3 < c < p/2

def rightTriangles(p: int) -> int:
    clo = (p // 3) + 1
    chi = (p // 2) + 1
    solns = 0
    test = p**2
    for c in range(clo, chi):
        b = c - 1
        a = p - b - c
        #print(f"init values: {a}, {b}, {c}")
        while (b >= a):
            #print(f"inside loop: {a}, {b}, {c}")
            #if (2 * (a * b + p * c) == test):
            if (a**2 + b**2 == c**2):
                solns += 1
            b -= 1
            a += 1
    return solns

max = 0
pmax = 0
for p in range(12, 1001):
    res = rightTriangles(p)
    if res > max:
        max = res
        pmax = p
print(pmax, max)


### testing ###
res = rightTriangles(120)
assert res == 3, f"Failed. Returned {res}"

print("All tests passed!")

# comment to test vs code git integration

