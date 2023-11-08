from itertools import permutations
from collections import deque
def solution(expression):
    answer = 0
    answer_list = []
    prior = []
    for exp in expression:
        if exp == "+" or exp == "*" or exp == "-":
            prior.append(exp)
    prior = set(prior)
    list(prior)
    cases = list(permutations(prior, len(prior)))
    for case in cases:
        priority = {}
        i = 0
        for check in case:
            priority[check] = i
            i += 1
        print(priority)
        answer_list.append(calcul(priority, expression))

    print(answer_list)        
    answer = max(answer_list)
    
    
    return answer

def calcul(priority , expression):
    op_stack = []
    num_stack = []
    get_num = deque()
    num = ''
    for exp in expression:    
        if exp == '-' or exp == '*' or exp == '+':
            
            get_num.append(int(num))
            num = ''
        else: num += exp
    get_num.append(int(num))
    
    #print(get_num)

    for exp in expression:
        result = 0
        if exp == '-' or exp == '*' or exp == '+':
            #print(exp)
            num_stack.append(get_num.popleft())
            
            if len(op_stack) == 0:
                op_stack.append(exp)
                
            else:
                if priority[op_stack[-1]] <= priority[exp]:
                    #print(num_stack)
                    while priority[op_stack[-1]] <= priority[exp]:
                        number2 = num_stack.pop()
                        number1 = num_stack.pop()
                        cal = op_stack.pop()
                        #print(num_stack)
                        if cal == '-':
                            num_stack.append(number1 - number2)
                        if cal == '+':
                            num_stack.append(number1 + number2)
                        if cal == '*':
                            num_stack.append(number1 * number2)
                        if len(op_stack) == 0:
                            break
                    op_stack.append(exp)
                if priority[op_stack[-1]] > priority[exp]:
                    op_stack.append(exp)
              
    #print(op_stack)
    #print(num_stack)
    #print(get_num)
    num_stack.append(get_num.popleft())
    while len(op_stack) != 0:
         
         number2 = num_stack.pop()
         number1 = num_stack.pop()
         cal = op_stack.pop()
                 
         if cal == '-':
             num_stack.append(number1 - number2)
         if cal == '+':
             num_stack.append(number1 + number2)
         if cal == '*':
             num_stack.append(number1 * number2)

        
    return abs(num_stack[0])
solution("100-200*300-500+20")