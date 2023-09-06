import unittest, time

def square_chain(x):
    while (x != 1 and x != 89):
        res = 0
        for digit in str(x):
            d = int(digit)
            res += d**2
        x = res
    if x == 1:
        return False
    return True

start = time.perf_counter()
count = 0
limit = 10000000
for x in range(1, limit):
    if square_chain(x):
        count += 1
end = time.perf_counter()
print(count)
print(f"Runtime: {end - start:0.2f}s")

class TestSquareChain(unittest.TestCase):
    def testArrivesAtOne(self):
        self.assertFalse(square_chain(44))

    def testArrivesAtEightyNine(self):
        self.assertTrue(square_chain(85))
        self.assertTrue(square_chain(145))

#unittest.main()