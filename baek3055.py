from collections import deque
R , C = list(map(int, input().split()))

matrix = []
for _ in range(R):
    matrix.append(list(map(str, input())))
wet = [[False for _ in range(C)] for _ in range(R)]
visit = [[False for _ in range(C)] for _ in range(R)]

water = deque()
rock = []
monster = deque()
dx =[0, 0, 1 ,-1]
dy =[1, -1 , 0, 0]

for i in range(R):
    for j in range(C):
        if matrix[i][j] == 'D':
            endpoint = [i, j]
        elif matrix[i][j] == 'S':
            monster.append([i,j])
            visit[i][j] = True
        elif matrix[i][j] == 'X':
            rock.append([i,j])
            wet[i][j] = True
        elif matrix[i][j] == '*':
            water.append([i,j])
            wet[i][j] = True

move = 0

flag = False

while(endpoint not in monster):
    #print(monster)
    wtemp = deque()
    mtemp = deque()
    if len(monster) == 0:
        #print(move)
        flag = True
        break
    while(water):
        x, y = water.popleft()
        for i in range(4):
            newx = x + dx[i]
            newy = y + dy[i]
            if 0 <= newx < R and 0 <= newy < C:
                if wet[newx][newy] == False and [newx , newy] != endpoint:
                    wet[newx][newy] = True
                    wtemp.append([newx,newy])
    while(monster):
        x, y = monster.popleft()
        for i in range(4):
            newx = x + dx[i]
            newy = y + dy[i]
            if 0 <= newx < R and 0 <= newy < C:
                if wet[newx][newy] == False and visit[newx][newy] == False:
                    visit[newx][newy] = True
                    mtemp.append([newx,newy])
    water = wtemp
    monster = mtemp
    move += 1
if flag:
    print("KAKTUS")
else:
    print(move)





        