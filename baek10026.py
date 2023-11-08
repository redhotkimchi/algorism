from collections import deque
N = int(input())
matrix = []
for _ in range(N):
    matrix.append(list(input()))
#print(matrix)

dx = [-1, 1, 0 , 0]
dy = [0 , 0, 1, -1]

deq = deque()

normal = [[False for _ in range(N)] for _ in range(N)]
blind = [[False for _ in range(N)] for _ in range(N)]

normal_count = 0
blind_count = 0

for i in range(N):
    for j in range(N):
        if normal[i][j] == False:
            normal[i][j] = True
            deq.append([i,j])
            normal_count +=1
            while(deq):
                #print("a")
                x, y = deq.popleft()
                color = matrix[x][y]
                for k in range(4):
                    newx = x + dx[k]
                    newy = y + dy[k]
                    if 0 <= newx < N and 0 <= newy < N:
                        if color == matrix[newx][newy] and normal[newx][newy] == False:
                            normal[newx][newy] = True
                            deq.append([newx,newy])
                        
for i in range(N):
    for j in range(N):
        if blind[i][j] == False:
            blind[i][j] = True
            #print(blind)
            deq.append([i,j])
            blind_count +=1
            while(deq):
                #print("a")
                x, y = deq.popleft()
                color = matrix[x][y]
                if color == 'R' or color == 'G':
                    for k in range(4):
                        newx = x + dx[k]
                        newy = y + dy[k]
                        if 0 <= newx < N and 0 <= newy < N:
                            if blind[newx][newy] == False:
                                if matrix[newx][newy] == 'R' or matrix[newx][newy] == 'G':
                                    blind[newx][newy] = True
                                    deq.append([newx,newy])
                else:
                    for k in range(4):
                        newx = x + dx[k]
                        newy = y + dy[k]
                        if 0 <= newx < N and 0 <= newy < N:
                            if color == matrix[newx][newy] and blind[newx][newy] == False:
                                blind[newx][newy] = True
                                deq.append([newx,newy])
            
#print(blind)
print(normal_count, blind_count)
