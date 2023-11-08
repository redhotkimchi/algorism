N, S = list(map(int, input().split()))

numbers = list(map(int, input().split()))

prenumbers = []
num = 0
for n in numbers:
    num += n
    prenumbers.append(num)
#print(prenumbers)

answer = float("inf")
if numbers[0] >= S:
    answer = 1
if prenumbers[-1] == S:
    answer = len(numbers)

for start in range(len(prenumbers)-1):
    end = start + 1
    
    while(prenumbers[end] - prenumbers[start] < S ):
        end += 1
        if end == len(prenumbers):
            break
    if end == len(prenumbers):
        if prenumbers[end-1] - prenumbers[start] >= S:
            answer = min(answer, end - start)
    else:
        answer = min(answer, end - start)
if prenumbers[-1] < S:
    print(0)

else:
    print(answer)
    