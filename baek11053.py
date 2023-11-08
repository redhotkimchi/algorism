N = int(input())
numbers = list(map(int, input().split()))

DP = [0 for _ in range(N)]

DP[0] = numbers[0]
for n in numbers:
    DP[i] = [i]



print(DP)
print(max(map(lambda x : x[1], DP[-1])))



