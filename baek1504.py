import heapq
N , E = list(map(int, input().split()))

graphs = [float("inf") for x in range(N+1)]
#print(graphs)

dic = {}
for i in range(1, N+1):
    dic[i] = []
for _ in range(E):
    a, b, w = list(map(int, input().split()))
    dic[a].append((w,b))
    dic[b].append((w,a))

v1, v2 = list(map(int, input().split()))
def dike(start, end):
    graphs[start] = 0
    heap = []
    heapq.heappush(heap, (0,start))
    while(heap):
        direc, b = heapq.heappop(heap)
        #print(heap)
        for w, c in dic[b]:
            temp = graphs[c]
            graphs[c] = min(graphs[c], direc + w)
            if temp != graphs[c]:
                #print(111111111111111)
                heapq.heappush(heap, (graphs[c], c))
    

# for w,b in dic[v1]:
#     if b == v2:
#         v1v2 = w
#         break
#     else:
#         v1v2 = 0


#stov1
dike(1, v1)
stov1 = graphs[v1]
stov2 = graphs[v2]
graphs = [float("inf") for x in range(N+1)]
#stov
#v1tov2
dike(v1, v2)
v12end = graphs[N]
v12 = graphs[v2]
graphs = [float("inf") for x in range(N+1)]
#v2tov2
dike(v2,v1)
v21 = graphs[v1]
v21end = graphs[N]

answer = min(stov1 + v12 + v21end, stov2+v21+v12end)


if answer == float("inf"):
    print(-1)
else:
    print(answer)

