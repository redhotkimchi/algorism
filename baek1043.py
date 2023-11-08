N , M = list(map(int, input().split()))

root = [x for x in range(N+1)]
def find(x):
    if root[x] != x:
        root[x] = find(root[x])
    return root[x]

def union(x, y):
    x = find(x)
    y = find(y)
    if x < y:
        root[y] = x
    else:
        root[x] = y

answer = 0
allcase = []
al = list(map(int, input().split()))
if len(al) >= 2:
    already = al[1:]
    for _ in range(M):
        guest = list(map(int, input().split()))[1:]
        if len(guest) >= 2:
            for i in range(len(guest)-1):                
                union(guest[i],guest[i+1])
                    #union(cases[j],cases[i])

        allcase.append(guest)

    for i in range(N+1):
        find(i)
    for a in already:
        lie = root[a]
        for i in range(len(root)):
            if root[i] == lie:
                root[i] = 0
    answerset = []
    for i in range(len(root)):
        if root[i] != 0:
            answerset.append(i)
    #print(answerset)
    for c in allcase:
        if set(answerset) >= set(c):
            answer += 1
else:
    for _ in range(M):
        cases = list(map(int, input().split()))
    answer = M
print(answer)    
