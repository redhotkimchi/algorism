from ast import Pass


def solution(s):
    answer = -1
    
    strings = list(s)

    answer_stack = []

    for a in strings:
        if len(answer_stack):
            if answer_stack[-1] == a:
                answer_stack.pop()
            else: answer_stack.append(a)
            
        else: answer_stack.append(a)

    if len(answer_stack):
        answer = 0
    else: answer = 1
    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    print(answer)

    return answer

s = 'baabaa'

solution(s)