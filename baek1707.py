from collections import deque
import sys
input = sys.stdin.readline
K = int(input())
for _ in range(K):
    V ,E = list(map(int, input().split()))
    nodes = [False] * (V+1)
    graphs = {}
    for i in range(1,V+1):
        graphs[i] = []
    for _ in range(E):
        a , b = list(map(int, input().split()))
        graphs[a].append(b)
        graphs[b].append(a)
    # deq.append((1,0))
    # left.append(1)
    # flag = True
    # while(deq):
    #     index, dir = deq.popleft()    
    #     if flag == False:
    #         break
    #     for n in graphs[index]:
    #         if nodes[n] == False:
    #             if dir == 0:
    #                 if n in left:
    #                     flag = False
    #                     break
    #                 else:
    #                     right.append(n)
    #                     nodes[n] = True
    #                     deq.append((n,1))
    #             elif dir == 1:
    #                 if n in right:
    #                     flag = False
    #                     break
    #                 else:
    #                     left.append(n)
    #                     nodes[n] = True
    #                     deq.append((n,0))
    #         else:
    #             if dir == 0:
    #                 if n in left:
    #                     flag = False
    #                     break
    #             elif dir == 1:
    #                 if n in right:
    #                     flag = False
    #                     break
    def bfs(a):
        left = []
        right = []
        deq = deque()
        deq.append((a,0))
        left.append(a)
        flag = True
        while(deq):
            index, dir = deq.popleft()    
            if flag == False:
                break
            for n in graphs[index]:
                if nodes[n] == False:
                    if dir == 0:
                        if n in left:
                            flag = False
                            break
                        else:
                            right.append(n)
                            nodes[n] = True
                            deq.append((n,1))
                    elif dir == 1:
                        if n in right:
                            flag = False
                            break
                        else:
                            left.append(n)
                            nodes[n] = True
                            deq.append((n,0))
                else:
                    if dir == 0:
                        if n in left:
                            flag = False
                            break
                    elif dir == 1:
                        if n in right:
                            flag = False
                            break
        return flag
    for i in range(1, V+1):
        if nodes[i] == False:
            flag = bfs(i)
            if flag == False:
                break

    if flag:
        print("YES")
    else:
        print("NO")


