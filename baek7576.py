from collections import deque
M, N = list(map(int,input().split()))
matrix = []
for _ in range(N):
    matrix.append(list(map(int, input().split())))

day = 0
#print(matrix)
dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

allcase = deque()
startdeq = deque()

for i in range(N):
    for j in range(M):
        if matrix[i][j] == 1:
            startdeq.append([i,j])
allcase.append(startdeq)

while(allcase):
    deq = allcase.popleft()
    #print(deq)
    new_deq = deque()
    day += 1
    while(deq):
        x, y = deq.popleft()
        #print(x,y)
        for i in range(4):
            new_x = x + dx[i]
            new_y = y + dy[i]
            if 0 <= new_x < N and  0 <= new_y < M:
                if matrix[new_x][new_y] == 0:
                    
                    matrix[new_x][new_y] = 1
                    new_deq.append([new_x,new_y])
    #print(new_deq)
    if len(new_deq) != 0:
        allcase.append(new_deq)
day -= 1
for m in matrix:
    if 0 in m:
        day = -1
        break
#print(matrix)
print(day)
