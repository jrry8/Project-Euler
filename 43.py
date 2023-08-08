def permutation(lst):
    if len(lst) == 0:
        return []

    if len(lst) == 1:
        return [lst]

    l = []

    # Iterate the input(lst) and calculate the permutation
    for i in range(len(lst)):
       m = lst[i]

       # Extract lst[i] or m from the list.  remLst is
       # remaining list
       remLst = lst[:i] + lst[i+1:]

       # Generating all permutations where m is first
       # element
       for p in permutation(remLst):
           l.append([m] + p)
    return l

pandigitalNums = permutation([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
res = 0
for num in pandigitalNums:
    d345 = num[2] + num[3] + num[4]
    d567 = num[4] * 100 + num[5] * 10 + num[6]
    d678 = num[5] * 100 + num[6] * 10 + num[7]
    d789 = num[6] * 100 + num[7] * 10 + num[8]
    d8910 = num[7] * 100 + num[8] * 10 + num[9]
    if (num[3] % 2 == 0 and d345 % 3 == 0 and num[5] % 5 == 0 and
    d567 % 7 == 0 and d678 % 11 == 0 and d789 % 13 == 0 and d8910 % 17 == 0):
        for i in range(len(num)):
            res += num[-1-i] * (10 ** i)
print(res)
