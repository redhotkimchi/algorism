import copy


count = 0

def solution(numbers, target):
    global count
    answer = 0
    dfs(numbers, 0 , target)
    answer = count
    return answer

def dfs(numbers,index,target):
    global count
    if index == len(numbers):
        return
    if sum(numbers) < target:
        return

    new_numbers = copy.deepcopy(numbers)
    new_numbers[index] = -new_numbers[index]
    if sum(new_numbers) == target:
        count += 1
        
    dfs(new_numbers, index + 1, target)
    new_numbers[index] = -new_numbers[index]
    dfs(new_numbers, index + 1, target) 


    

numbers = [1, 1, 1, 1, 1]
target = 3

solution(numbers, target)