N, M = list(map(int, input().split()))
matrix =[]
for _ in range(N):
    matrix.append(list(map(int, input().split())))
global allvisit, maxvalue

allvisit = [[False for _ in range(M)] for _ in range(N)]
visit = [[False for _ in range(M)] for _ in range(N)]
maxvalue = float("-inf")

def search(matrix, value, count,visit,index):
    global allvisit, maxvalue
    x, y = index
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    value += matrix[x][y]
    if count == 4:
        maxvalue = max(value, maxvalue)
        return
    for i in range(4):
        newx = x + dx[i]
        newy = y + dy[i]
        if 0<=newx<N and 0<=newy<M:
            if visit[newx][newy] == False:
                visit[newx][newy] = True
                newindex = [newx, newy]
                search(matrix, value, count+1 , visit, newindex)
                visit[newx][newy] = False

for i in range(N):
    for j in range(M):
        dx = [0, 1, 0, -1]
        dy = [1, 0, -1, 0]
        allnum = matrix[i][j]
        count = 1
        for d in range(4):
            newx = i + dx[d]
            newy = j + dy[d]
            if 0<=newx<N and 0<=newy<M:
                
                allnum += matrix[newx][newy]
                count += 1
        #print(count)
        if count == 4:
            maxvalue = max(allnum , maxvalue)

        if count == 5:
            #print("aa")
            for d in range(4):
                newx = i + dx[d]
                newy = j + dy[d]
                temp = allnum - matrix[newx][newy]
                #print(temp)
                maxvalue = max(temp , maxvalue)

for i in range(N):
    for j in range(M):
        visit[i][j] = True
        search(matrix, 0, 1, visit, [i,j])
        visit[i][j] = False

print(maxvalue)