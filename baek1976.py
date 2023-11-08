N = int(input())
M = int(input())

root = [i for i in range(N)]

def find(x):
    if root[x] != x:
        root[x] = find(root[x])     
    return root[x]
def union(x , y):
    x = find(x)
    y = find(y)
    if x < y:
        root[y] = x
    else:
        root[x] = y 

for i in range(N):
    case = list(map(int, input().split()))
    for j in range(N):
        if case[j] == 1:
            union(i,j)
            
plan = list(map(int, input().split()))

flag = True
test = root[plan[0]-1]
for p in plan:
    if root[p-1] != test:        
        flag = False
        break 
if flag:
    print("YES")
else:
    print("NO")