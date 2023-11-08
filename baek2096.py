from copy import deepcopy
N = int(input())
matrix = []
for _ in range(N):
    matrix.append(list(map(int, input().split())))

maxdp = deepcopy(matrix[0])
mindp = deepcopy(matrix[0])
for i in range(1, N):
    maxtemp = [0,0,0]
    mintemp = [0,0,0]
    maxtemp[0]=max(maxdp[0] + matrix[i][0] , maxdp[1] + matrix[i][0])
    maxtemp[1]=max(maxdp[0] + matrix[i][1] , maxdp[1] + matrix[i][1], maxdp[2] + matrix[i][1])
    maxtemp[2]=max(maxdp[1] + matrix[i][2] , maxdp[2] + matrix[i][2])
    mintemp[0]=min(mindp[0] + matrix[i][0] , mindp[1] + matrix[i][0])
    mintemp[1]=min(mindp[0] + matrix[i][1] , mindp[1] + matrix[i][1], mindp[2] + matrix[i][1])
    mintemp[2]=min(mindp[1] + matrix[i][2] , mindp[2] + matrix[i][2])
    for j in range(3):
        maxdp[j] = maxtemp[j]
        mindp[j] = mintemp[j]
    del mintemp, maxtemp

print(max(maxdp), min(mindp))

