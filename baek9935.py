string = list(input())
bomb = list(input())
expl = len(bomb)
stack = []
for s in string:    
    stack.append(s)
    if s == bomb[-1]:
        if len(stack) >= expl-1:
            #print("".join(stack[-(expl):]))
            if "".join(stack[-(expl):]) == "".join(bomb):
                #print("aa")
                for _ in range(expl):
                    stack.pop()
if len(stack) == 0:
    print("FRULA")
else:
    print("".join(stack))
