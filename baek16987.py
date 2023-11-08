from collections import deque
from copy import deepcopy
N = int(input())
egg_list = []
for _ in range(N):
    egg_list.append(list(map(int, input().split())))
global max_num
max_num = 0

#앞이 내구도
#뒤가 무게
def dfs(egg_list, hand_index):
    global max_num
    size = len(egg_list)
    count = 0
    #print(egg_list)
    if hand_index >= len(egg_list):
        for egg in egg_list:
            if egg[0] < 0:
                count += 1
        max_num = max(max_num, count)
        return
    HS = egg_list[hand_index][0]
    if HS <= 0:
        while(True):
            hand_index += 1
            if hand_index >= size:
                for egg in egg_list:
                    if egg[0] < 0:
                        count += 1
                max_num = max(max_num, count)
                return
            if egg_list[hand_index][0] > 0:
                break
    safe = 0
    for egg in egg_list:
        if egg[0] > 0:
            safe += 1
    if safe <= 1:
        for egg in egg_list:
            if egg[0] < 0:
                count += 1
        max_num = max(max_num, count)
        return
    for t in range(size):
        temp = deepcopy(egg_list)
        if t != hand_index:
            if temp[t][0] > 0:
                temp[t][0] -= temp[hand_index][1]
                temp[hand_index][0] -= temp[t][1]
                dfs(temp, hand_index+1)
        
            
dfs(egg_list, 0)
print(max_num)


    