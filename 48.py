# Self Powers
# Find the last ten digits of the series
# 1**1 + 2**2 + ... + 1000**1000

import unittest

TRUNC = 10**10

def sumLastDigits(x, y):
    x %= TRUNC
    y %= TRUNC
    return (x+y) % TRUNC

def multLastDigits(x, y):
    x %= TRUNC
    y %= TRUNC
    ans = 0
    #TODO
    return 0

def powLastDigits(x, n):
    if n == 1:
        return x % TRUNC
    tmp = multLastDigits(x, x)
    ans = powLastDigits(tmp, n // 2)
    if n % 2 == 1:
        ans = multLastDigits(ans, x)
    return ans % TRUNC

def foo():
    ans = 0
    for i in range(1, 1001):
        cur = powLastDigits(i, i)
        ans = sumLastDigits(ans, cur)
    return ans

class TestSum(unittest.TestCase):
    def testFewDigits(self):
        self.assertEqual(sumLastDigits(0,0), 0)
        self.assertEqual(sumLastDigits(142, 5643), 5785)
        self.assertEqual(sumLastDigits(7,11), 18)

    def test(self):
        self.assertEqual(sumLastDigits(902834012353, 78329181114), 1163193467)
        self.assertEqual(sumLastDigits(19834756293, 97465928374), 7300684667)

class TestMult(unittest.TestCase):
    #TODO
    def test(self):
        self.assertEqual(0,0)

class TestPow(unittest.TestCase):
    #TODO
    def test(self):
        self.assertEqual(0,0)

unittest.main()