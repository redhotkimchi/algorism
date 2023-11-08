N = int(input())

DP = [0 for _ in range(N+1)]

for i in range(N+1):
    if i == 0 or i == 1:
        DP[i] = 0
    if i == 2:
        DP[i] = 3
    if i == 3:
        DP[i] = 0
    if i == 4:
        DP[i] = 11
    if i >4 and i % 2 == 0:
        DP[i] = (DP[i-2] + 3) + (2+DP[i-4])
print(DP[-1])
