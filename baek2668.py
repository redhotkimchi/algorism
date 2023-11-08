N = int(input())

numbers = [0]

dic = {}

global answer
answer = 0


visit = [False] * (N+1)
globalvisit = set()

for i in range(N):
    dic[i+1] = []

for i in range(N):
    n = int(input())
    numbers.append(n)
    dic[n].append(i+1)
def dfs(node,count):
    global answer
    if node in globalvisit:
        return
    if len(dic[node]) == 0:
        return
    for n in dic[node]:
        if visit[n] == False:
            visit[n] = True
            dfs(n,count+1)
            visit[n] = False
        else:
            for i, v in enumerate(visit):
                if v == True:
                    globalvisit.add(i)
            answer += count
for i in range(1, N+1):
    visit[i] = True
    dfs(i, 1)
    visit[i] = False
answerlist = list(globalvisit)
print(answer)
for a in sorted(answerlist):
    print(a)

        

