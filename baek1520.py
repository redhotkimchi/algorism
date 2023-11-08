
import sys
M, N = list(map(int, sys.stdin.readline().split()))
matrix = []
for _ in range(M):
    matrix.append(list(map(int, sys.stdin.readline().split())))

DP = [[0 for _ in range(N)] for _ in range(M)]
dx = [-1, 1, 0 , 0]
dy = [0, 0, -1, 1]

# while(deq):
#     #print(deq)
#     x,y = deq.popleft()
#     for i in range(4):
#         newx = x + dx[i]
#         newy = y + dy[i]
#         if 0 <= newx < M and 0 <= newy < N :            
#             if matrix[newx][newy] < matrix[x][y]:
#                 for j in range(4):
#                     DP[i][newx][newy] += DP[j][x][y]
#                 deq.append([newx,newy])
#     print(DP[1][2][3])

# for D in DP:
#     print(";;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;")
#     for P in D:
#         print(P)


def dfs(x, y, DP, matrix):
    global dx, dy
    for i in range(4):
        #print("aa")
        newx = x + dx[i]
        newy = y + dy[i]
        if 0 <= newx < M and 0 <= newy < N :            
            if matrix[newx][newy] < matrix[x][y]:
                
                DP[newx][newy] += 1
                
                #visit[i][newx][newy] = True
                dfs(newx, newy, DP, matrix)

dfs(0, 0, DP, matrix)
# for D in DP:
#     print(D)
print(DP[M-1][N-1])

