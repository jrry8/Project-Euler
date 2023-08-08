# Champernowne's constant

n = 0
res = 1
for i in range(1, 1000000):
    num = str(i)
    for digit in num:
        n += 1
        if (n == 100 or n == 1000 or n == 10000 or n == 100000 or n == 1000000):
            print(f"n = {n}, digit = {digit}")
            res *= int(digit)
print(res)