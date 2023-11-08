T = int(input())
answer = []
for _ in range(T):
    N = int(input())
    stickers = []
    DP = [[0,0,0] for _ in range(N)]
    for _ in range(2):
        stickers.append(list(map(int , input().split())))
    DP[0][0] = stickers[0][0] #위 뜯었을때
    DP[0][1] = stickers[1][0] #아래 뜯었을떄
    DP[0][2] = 0 #안뜯었을때
    for i in range(1,N):
        DP[i][0] = max(stickers[0][i] + DP[i-1][1],stickers[0][i] + DP[i-1][2])
        DP[i][1] = max(stickers[1][i] + DP[i-1][0], stickers[1][i]+DP[i-1][2])
        DP[i][2] = max(DP[i-1][0], DP[i-1][1])
    answer.append(max(DP[-1]))
for a in answer:
    print(a)
