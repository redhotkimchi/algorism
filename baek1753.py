import heapq
from collections import deque

V, E = list(map(int, input().split()))
start = int(input())

nodes = [float("inf")]*(V+1)

# nodes[start] = 0

graph = {}
for i in range(1, V+1):
    graph[i] = []

for _ in range(E):
    a, b, w = list(map(int, input().split()))
    # heapq.heappush(graph[a],(w,b))
    # heapq.heappush(graph[b],(w,a))
    graph[a].append((w,b))
heap = []
heapq.heappush(heap , (0, start))
nodes[start] = 0
while(heap):
    w, cur = heapq.heappop(heap)
    if nodes[cur] < w:
        continue
    for value in graph[cur]:
        nextw, nextnode = value
        if nodes[cur] + nextw < nodes[nextnode]:
            nodes[nextnode] = nodes[cur] + nextw
            heapq.heappush(heap , value)

for i in range(1, V+1):
    if nodes[i] == float("inf"):
        print("INF")
    else:
        print(nodes[i])
        


