N = int(input())
nums = []
for _ in range(N):
    r , c = list(map(int, input().split()))
    nums.append([r,c])

DP = [[0,0,0] for _ in range(N)]
for i, n in enumerate(nums):
    DP[i][2] = n

DP[0][1] = DP[0][2]

for i in range(1, N):
    if i == 1:
        DP[1][0] = DP[0][2][0] * DP[0][2][1] * DP[1][2][1]
        DP[1][1] = [DP[0][2][0],DP[1][2][1]]

    else:
        DP[i][0] = min(DP[i-1][0] + (DP[i-1][1][0]*DP[i-1][1][1]*DP[i][2][1]), DP[i-2][0] + DP[i-2][1][0]*DP[i-2][1][1]*DP[i-1][2][1] + DP[i-1][1][0]*DP[i-1][1][1]*DP[i][2][1])
        DP[i][1] = [DP[i-2][1][0], DP[i][2][1]]
print(DP)
print(DP[-1][0])