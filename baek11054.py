N = input()
nums = list(map(int, input().split()))
DP = [[0 for _ in range(N)] for _ in range(N)]

for i in range(N):
    DP[i][0] = 1

for i in range(N):
    change = 0
    for j in range(i, N):
        if  i == j:
            DP[i][j] = 1
        elif nums[j-1] > nums[j]:
            pass
        elif nums[j-1] < nums[j]:
            DP[i][j] = DP[i][j] + 1

