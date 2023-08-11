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

#The last three consecutive numbers to have three distinct prime factors are 644, 645, 646
def findFirstFour():
    count = 0
    curNum = 647
    limit = 30000
    while (count < 4 and curNum < limit):
        if numDistinctPrimeFactors(curNum) == 4:
            count += 1
            curNum += 1
        else:
            count = 0
            curNum += 3
    ans = curNum
    return [x for x in range(ans-3, ans+1)]

print(findFirstFour())

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
    
#unittest.main()
