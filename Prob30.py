def powersum(n: int, p: int):
    sum = 0
    for d in str(n):
        sum += int(d) ** p
    if (sum == n):
        return True
    return False

res = []
sum = 0
for i in range(10, 1_000_000):
    if (powersum(i, 5)):
        res.append(i)
        sum += i
print(res, sum)


