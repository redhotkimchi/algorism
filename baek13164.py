N , K = list(map(int, input().split()))
kids = list(map(int, input().split()))

dif = []
for i in range(len(kids)-1):
    dif.append(kids[i+1]-kids[i])

dif.sort()

cost = 0

for i in range(N-K):
    cost += dif[i]
 
print(cost)