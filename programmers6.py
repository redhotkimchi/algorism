import math
def solution(n, words):
    answer = []
    already = []
    done = True

    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    for word in words:
        if word in already:
            already.append(word)
            done = False
            break
        if len(already):
            if already[-1][-1] != word[0]:
                already.append(word)
                done = False
                break
            else: 
                already.append(word)
                
        else: already.append(word)
            
    if done:
        answer = [0,0]
    else:
        a = len(already)%n
        if a == 0: a = n
        b = math.ceil(len(already)/n)
        answer = [a,b]
    print(answer)

    return answer

n = 3
words = ["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]
solution(n, words)