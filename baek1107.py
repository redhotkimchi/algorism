N = list(str(input()))
broken = int(input())
brokelist = list(map(int, input().split()))

remote = [True] * 10

number = []
for n in N:
    number.append(int(n))

for b in brokelist:
    remote[b] = False