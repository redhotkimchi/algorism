matrix = []
for _ in range(5):
    temp = list(map(str, input()))
    matrix.append(temp)
for m in matrix:
    print(m)
dx = [-1 , 1, 0, 0]
dy = [0, 0, -1, 1]

global count
count = 0
visit = [[False for _ in range(5)] for _ in range(5)]

def dfs(matrix, visit,x, y, prince, allc):
    global count
    #print(allc)
    if 0 <= x < 5 and 0 <= y < 5:
        # if visit[x][y] == True:
        #     return
        
        allc += 1
        if matrix[x][y] == "S":
            prince += 1
        if allc == 7:
            #print("aa")
            if prince >= 4:
                for v in visit:
                    print(v)
                count += 1
            return
        else:
            for d in range(4):
                newx = x + dx[d]
                newy = y + dy[d]
                if 0 <= newx < 5 and 0 <= newy < 5:
                    visit[newx][newy] = True
                    dfs(matrix, visit, newx,newy,prince, allc)
                    visit[newx][newy] = False

for i in range(5):
    for j in range(5):
        if matrix[i][j] == "S":
            visit[i][j] = True
            for d in range(4):
                newx = i + dx[d]
                newy = j + dy[d]
                dfs(matrix, visit, newx, newy, 1, 1)
                
print(count)