n,k = map(int, input().split())
coins = list()

for _ in range(n):
    coin = int(input())
    coins.append(coin)

result = 0

for coin in sorted(coins,reverse=True):
    if k // coin == 0:
        continue
    num = k // coin
    result += num
    k = k % coin
    
print(result)