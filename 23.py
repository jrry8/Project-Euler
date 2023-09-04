import math

# find all abundant numbers < 28123
# using above, find all sums of two abundant numbers that are <= 28123
# all that cannot be written as sum of two abundant numbers =
#   1 + ... + 28123 - (all sums of two abundant numbers <= 28123)

# precond: n is positive integer
def divisorSum(n: int) -> int:
    if (n == 1):
        return 1
    divisors = {1}
    for i in range(2, int(math.sqrt(n)) + 1):
        if (n % i == 0):
            divisors.add(i)
            divisors.add(int(n / i))
    res = 0
    for x in divisors:
        res += x
    return res

abund = []
for i in range(1, 28123):
    if (divisorSum(i) > i):
        abund.append(i)
#print(abund)

abund_sums = set()
for i in range(len(abund)):
    for j in range(i, len(abund)):
        tmp = abund[i] + abund[j]
        if (tmp <= 28123):
            abund_sums.add(tmp)
#print(abund_sums)

abund_total = 0
for x in abund_sums:
    abund_total += x
total = 0
for x in range(1, 28124):
    total += x
print(total - abund_total)