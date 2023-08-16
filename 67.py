# Maximum Path Sum II

import unittest

f = open("0067_triangle.txt", "r")

x0 = int(f.readline())
tmp = f.readline().split()
x1, x2 = int(tmp[0]), int(tmp[1])

dp = [x0+x1, x0+x2]

for x in f:
    prev = dp
    nums = x.split()
    n = len(nums)
    dp = [0] * n
    dp[0] = int(nums[0]) + prev[0]
    for i in range(1, n-1):
        dp[i] = int(nums[i]) + max(prev[i], prev[i-1])
    dp[n-1] = int(nums[n-1]) + prev[-1]

print(max(dp))