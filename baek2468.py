from collections import deque
N = int(input())
matrix = []
for _ in range(N):
    matrix.append(list(map(int, input().split())))
maxnum = 0
maxheight = max(map(max , matrix))
dx = [-1, 0, 1 , 0]
dy = [0, 1, 0, -1]
for rain in range(maxheight):
    count = 0
    if rain == 0:
        maxnum = max(maxnum, 1)
    else:
        
        visit = [[False for _ in range(N)] for _ in range(N)]
        deq = deque()
        for i in range(N):
            for j in range(N):
                if visit[i][j] == True:
                    continue
                if matrix[i][j] <= rain:
                    visit[i][j] = True
                    continue
                else:
                    count += 1
                    deq.append([i,j])
                    while(deq):
                        x ,y = deq.popleft()
                        for m in range(4):
                            nextx = x + dx[m]
                            nexty = y + dy[m]
                            if 0<= nextx < N and 0<= nexty < N:
                                if visit[nextx][nexty] == False:
                                    if matrix[nextx][nexty] > rain:
                                        deq.append([nextx,nexty])
                                        visit[nextx][nexty] = True
                                    else:
                                        visit[nextx][nexty] = True
    maxnum = max(maxnum, count)
print(maxnum)