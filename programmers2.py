def solution(brown, yellow):
    answer = []
    answer_list = []
    yellow_tile = []
    all_tile = brown + yellow

    for b in range(3, brown + 1):
         for a in range(b, brown + 1):
             if a * b == all_tile:
                if a + b == brown/2 + 2:

                    answer = [a, b]

    return answer


brown = 10
yellow = 2

solution(brown,yellow)