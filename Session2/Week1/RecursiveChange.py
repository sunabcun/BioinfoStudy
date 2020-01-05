import math

def RecursiveChange(money, Coins):
    if money == 0:
        return 0
    MinNumCoins = math.inf
    for i in range(len(Coins)-1):
        if money >= Coins[i]:
            NumCoins = RecursiveChange(money - Coins[i], Coins)
            if NumCoins +1 < MinNumCoins:
                MinNumCoins = NumCoins + 1
    return MinNumCoins

Coins = (5, 4, 1)

print (RecursiveChange(22, Coins))