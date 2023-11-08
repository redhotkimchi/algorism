import math
def solution(n,a,b):
    answer = 0
    number = n
    count = 0

    while n != 1:
        n /= 2
        count += 1
    print(count)
    for i in range(1, count + 1):
        if math.ceil(a / 2) == math.ceil(b / 2):
            answer = i
            break
        else:
            a = math.ceil(a/2)
            b = math.ceil(b/2)
    

    return answer

solution(1024,1,2)