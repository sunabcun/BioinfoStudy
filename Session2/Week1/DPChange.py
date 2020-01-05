import math
def DPChange(money, Coins):
    MinNumCoins = {0:0}
    for m in range(1, money+1):
        MinNumCoins[m] = math.inf
        for i in range(len(Coins)-1):
            if m >= Coins[i]:
                if MinNumCoins[m - Coins[i]] + 1 < MinNumCoins[m]:
                   MinNumCoins[m] = MinNumCoins[m - Coins[i]] + 1
                  # print (MinNumCoins[m])
    return MinNumCoins[money]



Coins = (24,23,20,15,5,3,1)
print (DPChange(18743, Coins))