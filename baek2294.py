N , K = list(map(int, input().split()))
DP = [float("inf")] * (K+1)
coins = []
for _ in range(N):
    coins.append(int(input()))
for i in range(1, K+1):
    for c in coins:
        if i == c:
            DP[i] = 1
        if i + c <= K:
            DP[i+c] = min(DP[i+c], DP[i] + 1)
if DP[-1] == float("inf"):
    print(-1)
else:
    print(DP[-1])

