from copy import deepcopy
N = int(input())
global matrix
matrix = [0 for _ in range(N)]
global count
count = 0
def dfs(index):
    global count, matrix
    if index == N - 1:
        pass
    for i in range(N):
        flag = False
        for j in range(index):
            if i == matrix[j] or abs(i - matrix[j]) == abs(index - j):
                #print("a")
                flag = True
        if flag == False:
            if index == N-1:
                #print(matrix)
                count += 1
                return
            else:
                matrix[index] = i
                dfs(index + 1)
        else: continue
dfs(0)
print(count)    
