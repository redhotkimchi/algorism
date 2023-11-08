from collections import deque
N, M = list(map(int , input().split()))

matrix = []

for _ in range(N):
    temp = list(map(int, input()))
    matrix.append(temp)
#print(matrix)

start_index = [0,0,1,0]
deq = deque()
deq.append(start_index)

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

visit = [[False for _ in range(M)] for _ in range(N)]
brokevisit = [[False for _ in range(M)] for _ in range(N)]

answer = []

if N == 1 and M == 1:
    answer.append(1)

while(deq):    
    #print(deq)
    x , y , count, block = deq.popleft()
    for i in range(4):
        newx = x + dx[i]
        newy = y + dy[i]
        if 0<= newx < N and 0 <= newy < M and visit[newx][newy] == False:
            if block == 1:
                if brokevisit[newx][newy] == False:

                    if matrix[newx][newy] == 0:
                        deq.append([newx,newy, count + 1, block])
                        brokevisit[newx][newy] = True
                        if newx == N -1 and newy == M-1:
                            brokevisit[newx][newy] = False
                            answer.append(count+1)
                                    
            else:
                if visit[newx][newy] == False:
                    if matrix[newx][newy] == 0:
                        deq.append([newx,newy, count + 1, block])
                        visit[newx][newy] = True
                        if newx == N -1 and newy == M-1:
                            visit[newx][newy] = False
                            answer.append(count+1)
                    else:
                        deq.append([newx,newy, count + 1, 1])
                        brokevisit[newx][newy] = True
                        if newx == N -1 and newy == M-1:
                            brokevisit[newx][newy] = False
                            answer.append(count+1)
if len(answer) == 0:
    print(-1)
else:
    print(min(answer))