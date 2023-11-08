list1 = list(input())
list2 = list(input())

DP = [[0 for _ in range(len(list1)+1)] for _ in range(len(list2)+1)]

for i in range(1, len(DP)):
    for j in range(1, len(DP[0])):
        if list1[j-1] == list2[i-1]:
            DP[i][j] = DP[i-1][j-1] + 1
            
print(max(map(max,DP)))