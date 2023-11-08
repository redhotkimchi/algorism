from copy import deepcopy
L, C = list(map(int, input().split()))
alpha = list(map(str, input().split()))
global mo ,ja
mo = []
ja = []
alpha.sort()
answer = []
for a in alpha:
    if a in ['a', 'e','i', 'o','u']:
        mo.append(a)
    else:
        ja.append(a)
#print(mo, ja)
case = []
#True 모음일 경우
#False 자음일 경우
def dfs(case , index, alpha, answer, mcount, jcount):
    global mo, ja
    tempcase = deepcopy(case)
    tempcase.append(alpha[index])
    print(tempcase)
    if alpha[index] in mo:
        mcount += 1
    else:
        jcount += 1
    # print(case)
    if len(tempcase) >= L:
        if mcount >= 1 and jcount >=  2:
            
            answer.append(tempcase)
            return
        else:
            return
    else:
        for i in range(index+1, len(alpha)):
            dfs(tempcase , i, alpha, answer, mcount, jcount)

for i in range(len(alpha)):
    dfs([],i, alpha, answer,0,0)
        
for a in answer:
    print("".join(a))
