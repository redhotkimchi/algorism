from collections import deque
N, d, k, c = list(map(int, input().split()))

sushies = []
for _ in range(N):
    sushies.append(int(input()))

cases = []

maxnum = 0

for start in range(N):
    end = start + k-1
    if end >= N:
        end = end - N
    if start < end:
        temp = set(sushies[start:end + 1])
        count = len(temp)
        #print(set(sushies[start:end + 1]))
        if c not in temp:
            count += 1
        maxnum = max(maxnum, count)
    elif start > end:
        a = sushies[0 : end +1]
        b = sushies[start : N]
        temp = set(a+b)
        #print(set(a+b))
        count = len(temp)
        if c not in temp:
            count += 1
        maxnum = max(maxnum, count)
    elif start == end:
        maxnum = max(maxnum , 1)

print(maxnum)
