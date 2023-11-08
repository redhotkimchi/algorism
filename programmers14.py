from re import L

flag = False
visit = [[0 for col in range(5)] for row in range(5)]

def solution(places):
    answer = []
    global flag,visit
    
    for case in places:
        flag = False
        search = [[0 for col in range(5)] for row in range(5)]
        for i in range(len(case)):
            
            for j in range(len(case[0])):
                if case[i][j] == 'P':
                    search[i][j] = 2
                if case [i][j] == 'X':
                    search[i][j] = -2
                if  case[i][j] == 'O':
                     search[i][j] = -1

        for i in range(5):
            if flag:
                break
            for j in range(5):
                if flag:
                    break
                count = 0
                if search[i][j] == 2:
                    #print("start, i, j",i, j)
                    visit = [[0 for col in range(5)] for row in range(5)]
                    dfs(i,j,search, 0, count)
                    
                
        if flag:
            answer.append(0)
        else: answer.append(1)

    print(answer)
    
    return answer

def dfs(i, j,search , energy,count):
    global flag, visit
    
    if i >= 5 or j >= 5 or j <0 or i <0:
        return
    if visit[i][j] == 1:
        return
    if search[i][j] == 4:
        return
    energy +=search[i][j]
    visit[i][j] = 1
    
    if energy < 0:
        return 
    if energy >= 0:
        if energy == 0 and search[i][j] != 2:
            #print("stop", i , j)
            return

        if search[i][j] == 2 and count != 0:
            print("energy , i , j",energy, i, j)
            flag = True
            return 
        else: 
            
            count += 1
            dfs(i+1, j,search, energy,count)
            dfs(i,j+1,search,energy,count)
            dfs(i, j-1,search, energy, count)


    

places = [["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]
solution(places)