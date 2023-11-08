N, M = list(map(int, input().split()))

dic = {}
for i in range(N):
    dic[i] = []

visited = [False for _ in range(N)]


global falg
flag = False

for _ in range(M):
    a , b = list(map(int, input().split()))
    dic[a].append(b)
    dic[b].append(a)
#print(dic)
def dfs(count, node, visited):
    #print(count)
    global flag
    if count >= 5:
        flag = True
        return
    else:
        for d in dic[node]:
            #print(d)
            if visited[d] == False:
                visited[d] = True
                dfs(count + 1 , d, visited)
                visited[d] = False
            # else:
            #     print("bb")
for i in range(N):
    visited[i] = True
    dfs(1, i, visited)
    visited[i] = False
    if flag:
        break
if flag:
    print(1)
else:
    print(0)