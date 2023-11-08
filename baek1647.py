import heapq
N , M = list(map(int, input().split()))

nodes = []
for i in range(N+1):
    nodes.append(i)

heap = []
for _ in range(M):
    a, b, w = list(map(int, input().split()))
    heapq.heappush(heap,(w, a, b))
def find(x):
    if nodes[x] != x:
        nodes[x] = find(nodes[x])
    return nodes[x]
def union(x, y):
    x = find(x)
    y = find(y)
    if x > y:
        nodes[x] = y
    else:
        nodes[y] = x

maxweight = 0
check = 0
allcost = 0
while(heap):
    
    if check == N-1:
        break
    w , a, b = heapq.heappop(heap)
    if find(a) != find(b):
        union(a, b)
        maxweight = max(maxweight, w)
        check += 1
        allcost += w

    else:
        continue
print(allcost-maxweight)

