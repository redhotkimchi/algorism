N = int(input())
M = int(input())
vip = []

DP = [0 for _ in range(N)]
DP[0] = 1

for _ in range(M):
    vip.append(int(input())-1)
if 0 in vip:
    DP[0] = 0
answers = []

if len(vip) == N:
    print(1)
elif len(vip) == 0:
    for i in range(1, len(DP)):
        if i == 1:
            DP[i] = 2
        else:
            DP[i] = DP[i-1] + DP[i-2]
    print(DP[-1])
else:
    for i in range(1, len(DP)):
        if i in vip:
            if DP[i-1] != 0:
                answers.append(DP[i-1])
            DP[i] = 0
            continue
        else:
            if DP[i-1] == 1:
                DP[i] = 2
            elif DP[i-1] == 0:
                DP[i] = 1
            else:
                DP[i] = DP[i-1] + DP[i-2]
    if DP[-1] != 0:
        answers.append(DP[-1])
#print(DP)
    answer = 1
    for a in answers:
        answer = answer * a
    #print(DP)
    print(answer)

