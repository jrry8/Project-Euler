# Distinct Prime Factors

import unittest, time

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
# tests numbers between start and end
def find(m, d, start, end):
    count = 0
    curNum = start
    while (count < m and curNum < end):
        if numDistinctPrimeFactors(curNum) == d:
            count += 1
        else:
            count = 0
        curNum += 1
    return curNum - m

start = time.perf_counter()
print(find(4, 4, 100000, 200000))
end = time.perf_counter()
print(f"Runtime: {end - start:0.2f}")

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
        self.assertEqual(find(2, 2, 0, 100), 14)
    
    def testThreeConsecThreeFactors(self):
        self.assertEqual(find(3, 3, 0, 1000), 644)
    
#unittest.main()
