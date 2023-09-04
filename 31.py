from typing import List

# How many different ways can n pence be made using the given coins
def coinChange(n: int, coins: List[int]) -> int:
    return coinChangeHelper(n, coins, 0)

def coinChangeHelper(n: int, coins: List[int], count: int) -> int:
    if (n == 0):
        return 1
    if not coins:
        return count
    if (n // coins[-1] == 0):
        return coinChangeHelper(n, coins[:-1], count)
    m = n // coins[-1]
    for i in range(m, 0, -1):
        N = n - (coins[-1] * i)
        count += coinChangeHelper(N, coins[:-1], 0)
    return coinChangeHelper(n, coins[:-1], count)


### testing ###
my_coins = [1, 2, 5, 10, 20, 50, 100, 200]
tmp = coinChange(5, my_coins)
if (tmp != 4):
    print("coinChange(5) incorrectly returned", tmp)
tmp = coinChange(0, my_coins)
if (tmp != 1):
    print("coinChange(0) incorrectly returned", tmp)
print(coinChange(200, my_coins))