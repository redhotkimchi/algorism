from collections import Counter
import sys
input = sys.stdin.readline
N = int(input())
A = []
B = []
C = []
D = []
for _ in range(N):
    a, b, c, d = list(map(int, input().split()))
    A.append(a)
    B.append(b)
    C.append(c)
    D.append(d)

AB = []
CD = []
for a in A:
    for b in B:
        AB.append(a + b)
for c in C:
    for d in D:
        CD.append(c + d)

AB.sort()
CD.sort()

dic = Counter(CD)


answer = 0

def binary_search(data):
    start = 0
    end = len(CD) - 1
    while start <= end:
        mid = (start + end) // 2
        if CD[mid] + data == 0:
            return CD[mid]
        elif CD[mid] + data > 0:
            end = mid - 1
        else:
            start = mid + 1
    return None

for ab in AB:
    value = binary_search(ab)
    if value != None:
        answer += dic[value]
    

print(answer)