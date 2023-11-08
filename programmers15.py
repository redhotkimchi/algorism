def solution(numbers, hand):
    answer = ''
    left_stack = [[3,0]]
    right_stack = [[3,2]]
    
    for case in numbers:
        #print(case)
        if case in [1,4,7]:
            answer += 'L'
            if case == 1:
                coordinate = [0,0]
            if case == 4:
                coordinate = [1,0]
            if case == 7:
                coordinate = [2,0]
            left_stack.append(coordinate)
            continue
        elif case in [3,6,9]:
            answer += 'R'
            if case == 3:
                coordinate = [0,2]
            if case == 6:
                coordinate = [1,2]
            if case == 9:
                coordinate = [2,2]
            right_stack.append(coordinate)
            continue
        # elif case == 0:
        #     if hand == "right":
        #         answer += 'R'
        #     if hand == "left":
        #         answer += 'L'
                
        elif case in [2,5,8,0]:
            if case == 0:
                coordinate = [3,1]
            if case == 2:
                coordinate = [0,1]
            elif case == 5: 
                coordinate = [1,1]
            elif case == 8:
                coordinate = [2,1]
            
            if dist(coordinate, left_stack[-1]) == dist(coordinate, right_stack[-1]):
                if hand == "right":
                    right_stack.append(coordinate)
                    answer += 'R'
                    continue
                if hand == "left":
                    left_stack.append(coordinate)
                    answer += 'L'
                    continue
            if dist(coordinate, left_stack[-1]) > dist(coordinate, right_stack[-1]):
                right_stack.append(coordinate)
                answer += 'R'
                continue
            if dist(coordinate, left_stack[-1]) < dist(coordinate, right_stack[-1]):
                left_stack.append(coordinate)
                answer += "L"
                continue
        
    return answer
def dist(a , b):
    return abs(a[0] - b[0]) + abs(a[1]-b[1])