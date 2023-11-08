from audioop import reverse
import math
def solution(citations):
    answer = 0
    citations.sort(reverse = True)
    for index in range(0,len(citations)):
        #print(index)
        if index == len(citations) -1: 
            
            return len(citations)
        h = citations[index]
        if h == citations[index + 1]:
            if len(citations[:index + 1]) >= h:
                answer = h
                print(answer)
                return answer  
        for h_index in range(h, citations[index + 1], -1):
            #print(h_index)
            if len(citations[:index + 1]) >= h_index:
                answer = h_index
                print(answer)
                return answer                

citations = [6, 6, 6, 6, 6, 6, 6, 6]
solution(citations)