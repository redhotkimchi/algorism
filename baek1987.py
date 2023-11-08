N, M = list(map(int, input().split()))
matrix = []
for _ in range(N):
    matrix.append(list(map(str, input())))

dx = [-1,1,0,0]
dy = [0,0,-1,1]

global answer
answer = 0

def dfs(visit,x,y, move):
    global answer
    #print(matrix)    
    for i in range(4):
        newx = x + dx[i]
        newy = y + dy[i]
        if 0<= newx < N and 0<= newy <M :
            if visit[ord(matrix[newx][newy])-65] == False:
                visit[ord(matrix[newx][newy])-65] = True
                dfs(visit,newx,newy,move + 1)
                visit[ord(matrix[newx][newy])-65] = False
            else:
                answer = max(answer, move)

visit = [False] * 26
visit[ord(matrix[0][0])-65] = True

dfs(visit, 0, 0, 1)

print(answer)