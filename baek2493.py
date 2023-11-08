from collections import deque
N = int(input())
towers = list(map(int, input().split()))

answer = [0] * N
stack = []
deq = deque()
for i, t in enumerate(towers):
    stack.append([i,t])

while(stack):
    i, t = stack.pop()
    if len(deq) == 0:
        deq.append([i,t])
        continue
    else:
        if deq[-1][1] > t:
            deq.append([i,t])
        else:
            while(deq):
                if deq[-1][1] > t:
                    break
                elif deq[-1][1] < t:
                    a, b = deq.pop()
                    answer[a] = i+1
            deq.append([i,t])

# print(deq)
for a in answer:
    print(a, end = " ")