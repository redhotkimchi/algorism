import sys
sys.setrecursionlimit(10000)
from collections import deque
N, Q = list(map(int, input().split()))

graph = [[float('inf') for _ in range(N+1)] for _ in range(N+1)]
visit = [[False for _ in range(N+1)] for _ in range(N+1)]

dic = {}
for i in range(1, N+1):
    dic[i] = []
for _ in range(N-1):
    a, b, u = list(map(int, input().split()))
    graph[a][b] = u
    graph[b][a] = u
    dic[a].append(b)
    dic[b].append(a)


def dfs(a, start, end, weight, visit):
        for j in dic[a]:
            if graph[a][j] != float("inf"):
                if j == end:
                      graph[start][j] = min(weight, graph[a][j])
                      graph[j][start] = min(weight, graph[a][j])
                      return
                else:
                    if visit[a][j] == False:
                        visit[a][j] = True
                        visit[j][a] = True
                        dfs(j, start , end, min(weight,graph[a][j]), visit)
                        visit[a][j] = False
                        visit[j][a] = False                    
        
# for i in range(1, N+1):
#     for j in range(1, N+1):
#          if i != j:
#             if graph[i][j] == float("inf"):
#                 visit[i][j] = True
#                 visit[j][i] = True
#                 dfs(i, i, j, graph[i][j], visit)
#                 visit[j][i] = False
#                 visit[i][j] = False
                
                       


for _ in range(Q):
    k, v = list(map(int, input().split()))
    for j in range(1, N+1):
         if graph[v][j] == float("inf"):
            visit[v][j] = True
            visit[j][v] = True
            dfs(v, v, j, graph[v][j], visit)
            visit[j][v] = False
            visit[v][j] = False
              
    count = 0
    for i in range(1, N+1):
        if graph[v][i] >= k and graph[v][i] != float("inf"):
            count += 1
    print(count)

