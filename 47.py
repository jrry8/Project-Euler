# Distinct Prime Factors

import unittest

def numDistinctPrimeFactors(x):
    pf = set()
    factor = 2
    while(x >= factor):
        if x % factor == 0:
            pf.add(factor)
            x //= factor
        else:
            factor += 1
    return len(pf)

# find the first m consecutive numbers to have d distinct prime factors
# tests numbers up to limit
def find(m, d, limit):
    count = 0
    curNum = 0
    while (count < m and curNum < limit):
        if numDistinctPrimeFactors(curNum) == d:
            count += 1
        else:
            count = 0
        curNum += 1
    return curNum - 1

class TestDistinctPrimeFactors(unittest.TestCase):
    def testOneFactor(self):
        self.assertEqual(numDistinctPrimeFactors(7), 1)
        self.assertEqual(numDistinctPrimeFactors(8), 1)

    def testTwoFactors(self):
        self.assertEqual(numDistinctPrimeFactors(14), 2)
        self.assertEqual(numDistinctPrimeFactors(15), 2)
    
    def testThreeFactors(self):
        self.assertEqual(numDistinctPrimeFactors(644), 3)
        self.assertEqual(numDistinctPrimeFactors(645), 3)
        self.assertEqual(numDistinctPrimeFactors(646), 3)

    def testFourFactors(self):
        self.assertEqual(numDistinctPrimeFactors(210), 4)
        self.assertEqual(numDistinctPrimeFactors(420), 4)
        self.assertEqual(numDistinctPrimeFactors(5700), 4)

class TestFind(unittest.TestCase):
    def testTwoConsecTwoFactors(self):
        self.assertEqual(find(2, 2, 100), 15)
    
    def testThreeConsecThreeFactors(self):
        self.assertEqual(find(3, 3, 1000), 646)
    
unittest.main()
