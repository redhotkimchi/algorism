import math
def solution(progresses, speeds):
    answer = []
    max = 0
    daycount_list = []
    for a,b in zip(progresses, speeds):
        daycount_list.append(math.ceil((100 - a)/b))

    stack = []
    for day in daycount_list:
        if(len(stack)):
            if max >= day:
                stack.append(day)
            else:
                answer.append(len(stack))
                stack.clear()
                stack.append(day)
                max = day
        else:
            max = day
            stack.append(day)
    answer.append(len(stack))
    print(answer)


    return answer

progresses = [93, 30, 55]
speeds = [1, 30, 5]
solution(progresses, speeds)