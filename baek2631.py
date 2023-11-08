import sys
N = sys.stdin.readline()
line = [0]
for i in range(int(N)):
    line.append(int(sys.stdin.readline()))
count = 0

DP = [1]*(int(N)+1)


for i in range(1, int(N)+1):
    for j in range(1 ,i):
        if line[j] <line[i]:
            DP[i] = max(DP[i] ,DP[j]+1)

print(int(N)-max(DP))