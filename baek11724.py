from collections import deque
N , M = input().split()
count = 0
graph = {}
visit = [0 for _ in range(int(N))]
for i in range(int(N)):
    graph[i] = []

deq = deque()

for i in range(int(M)):
    a , b = input().split()
    a = int(a)
    b = int(b)
    
    graph[a-1].append(b-1)
    graph[b-1].append(a-1)

for i in range(int(N)):
    if visit[i] == 1:
        continue
    else:
        if  len(graph[i]) == 0:
            visit[i] = 1
            count += 1
            continue
        count += 1
        visit[i] = 1
        for node in graph[i]:
            if visit[node] == 0:
                visit[node] = 1
                deq.append(node)
        while(deq):
            #print(deq)
            index = deq.popleft()
            visit[index] = 1
            for node in graph[index]:
                if visit[node] == 0:
                    visit[node] = 1
                    deq.append(node)
print(count)