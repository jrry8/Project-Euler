# Self Powers
# Find the last ten digits of the series
# 1**1 + 2**2 + ... + 1000**1000

import unittest

DIGITS = 10
TRUNC = 10 ** DIGITS

def sumLastDigits(x, y):
    x %= TRUNC
    y %= TRUNC
    return (x+y) % TRUNC

def multLastDigits(x, y):
    x %= TRUNC
    y %= TRUNC
    ans = 0
    i = 0
    for d in reversed(str(y)):
        tmp = (x % (10 ** (DIGITS-i))) * int(d)
        ans += (tmp * (10 ** i))
        i += 1
    return ans % TRUNC

# assuming n >= 1
def powLastDigits(x, n):
    if n == 1:
        return x % TRUNC
    tmp = multLastDigits(x, x)
    ans = powLastDigits(tmp, n // 2)
    if n % 2 == 1:
        ans = multLastDigits(ans, x)
    return ans % TRUNC

def foo(end):
    ans = 0
    for i in range(1, end+1):
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
    def test(self):
        self.assertEqual(multLastDigits(3, 5), 15)
        self.assertEqual(multLastDigits(17, 99), 1683)
        self.assertEqual(multLastDigits(100000, 1000000), 0)
        self.assertEqual(multLastDigits(357, 1029340475), 7474549575)

class TestPow(unittest.TestCase):
    def test(self):
        self.assertEqual(powLastDigits(2, 5), 32)
        self.assertEqual(powLastDigits(17, 5), 1419857)
        self.assertEqual(powLastDigits(19, 9), 2687697779)
        self.assertEqual(powLastDigits(11, 12), 8428376721)

class TestFinal(unittest.TestCase):
    def test(self):
        self.assertEqual(foo(10), 405071317)

#unittest.main()

print(foo(1000))