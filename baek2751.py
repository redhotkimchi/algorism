N = int(input())
number = []
for _ in range(N):
    i = int(input())
    number.append(i)
number.sort()
for n in number:
    print(n)
