from collections import deque
string = list(map(str, input()))
deq = deque(string)
prior = ['*','/']
par = ['(', ")"]
minor = ['+','-']
oper = ['*','/','+','-']
stack = []
answer = []
while(deq):
    num = deq.popleft()
    if num in prior:
        if len(stack) == 0:
            stack.append(num)
            continue
        
    elif num in minor:
        if len(stack) == 0:
            stack.append(num)
            continue
    elif num in par:
        if num == '(':
            stack.append(num)
            while(True):
                n = deq.popleft()
                if n == ')':
                    break
                elif n == '(':
                    stack.append(num)
    else:
        if len(answer) == 0:
            answer.append(num)
            continue
        else:
            pass


