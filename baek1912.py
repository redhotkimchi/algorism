N = int(input())
numbers = list(map(int, input().split()))

DP = [0] * N
DP[0] = numbers[0]
for i in range(1, N):
    DP[i] = max(0, DP[i-1]) + numbers[i]
answer = max(DP)
print(answer)
    