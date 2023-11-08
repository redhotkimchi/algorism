N = int(input())
numbers = list(map(int, input().split()))
answer = []

for i in range(N-1):
    flag = False
    for j in range(i+1, N):
        if numbers[i] < numbers[j]:
            flag = True
            answer.append(numbers[j])
            break
    if flag == False:
        answer.append(-1)
answer.append(-1)
for a in answer:
    print(a , end = " ")

