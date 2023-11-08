from collections import deque
N = int(input())
matrix = []
for _ in range(N):
    matrix.append(list(map(int, input().split())))
DP = [[0 for _ in range(N)] for _ in range(N)]
DP[0][0] = 1
visit = [[False for _ in range(N)] for _ in range(N)]
visit[0][0] = True
for i in range(N):
    for j in range(N):
        if i == N-1 and j == N-1:
            break
        if visit[i][j] == True:
            if j + matrix[i][j] < N:
                visit[i][j+matrix[i][j]] = True
                DP[i][j+matrix[i][j]] += DP[i][j]
            if i + matrix[i][j] < N:
                visit[i+matrix[i][j]][j] = True
                DP[i+matrix[i][j]][j] += DP[i][j]


print(DP[-1][-1])
