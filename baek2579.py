N = int(input())
stairs = []
for _ in range(N):
    stairs.append(int(input()))
DP = [[0,0] for _ in range(N)]
DP[0][0] = stairs[0]
DP[0][1] = stairs[0]
#[0][0] 다음으로 갈 수 없는 경우
#[0][1] 한계단 다음으로 갈 수 있는 경우
for i in range(1, N):
    if i == 1:
        DP[i][0] = stairs[i] + DP[0][0]
        DP[i][1] = stairs[i]
    else:
        DP[i][0] = stairs[i] + DP[i-1][1]
        DP[i][1] = max(stairs[i] + DP[i-2][0], stairs[i] + DP[i-2][1])
print(max(DP[-1]))

