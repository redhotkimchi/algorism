N, K = list(map(int, input().split()))
coins = []
DP = [0 for _ in range(K+1)]
for _ in range(N):
    coins.append(int(input()))
# print(coins)
DP[0] = 1
for c in coins:
    for price in range(len(DP)):
        if price < c:
            continue
        else:
            DP[price] += DP[price - c]
    # print(DP)
print(DP[-1])


