
N = int(input())
M = int(input())

answer = 0
matrix = []

for _ in range(M):
    links = list(map(int, input().split()))
    matrix.append(links)

matrix = sorted(matrix, key = lambda x : x[2])
#print(matrix)
unions = [i for i in range(N)]
visit = [False for _ in range(N)]
#print(unions)
def find_parent(parent , x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]
def union_parent(parent , a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b
for m in matrix:
    a , b , cost = m
    if find_parent(unions, a-1) != find_parent(unions, b-1):
        union_parent(unions, a-1,b-1)
        #print(a, b)
        answer += cost
#print(unions)
print(answer)