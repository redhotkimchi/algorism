def solution(commands):
    mergecheck = [[False for _ in range(51)] for _ in range(51)]
    values = [['EMPTY' for _ in range(51)] for _ in range(51)]
    parents = [[(i,j) for j in range(51)] for i in range(51)]
    
    def union(r1, c1, r2, c2):
        x1, y1 = find((r1, c1))
        x2, y2 = find((r2, c2))
        
        parents[x2][y2] = (x1, y1)
        
    def find(index):
        if parents[index[0]][index[1]] != index:
            parents[index[0]][index[1]] = find(parents[index[0]][index[1]])
        return parents[index[0]][index[1]]
    
    answer = []
    
    for command in commands:
        commandlist = command.split()
        option = commandlist[0]   
        if option == 'UPDATE':
            if len(commandlist) == 4:
                option, r, c, value = commandlist
                r = int(r)
                c = int(c)
                x, y = find((r,c))
                values[x][y] = value
            else:
                option, value1, value2 = commandlist
                for i in range(1, 51):
                    for j in range(1, 51):
                        if values[i][j] == value1:
                            values[i][j] = value2
        if option == 'MERGE':
            option, r1, c1, r2, c2 = commandlist
            r1 = int(r1)
            c1 = int(c1)
            r2 = int(r2)
            c2 = int(c2)
            x, y = find((r1, c1))
            x2, y2 = find((r2, c2))
            if values[x][y] == 'EMPTY':
                values[x][y] = values[x2][y2]
                union(r1, c1, r2, c2)
            else:
                values[x2][y2] = values[x][y]
                union(r2, c2, r1, c1)
            
        if option == 'UNMERGE':
            option, r, c = commandlist
            r = int(r)
            c = int(c)
            x, y = find((r, c))
            temp = values[x][y]
            for i in range(1, 51):
                for j in range(1, 51):
                    find((i,j))
            for i in range(1, 51):
                for j in range(1, 51):
                    if parents[i][j] == (x, y):
                        parents[i][j] = (i, j)
                        values[i][j] = "EMPTY"
            values[r][c] = temp
        if option == 'PRINT':
            option, r, c = commandlist
            r = int(r)
            c = int(c)
            x, y = find((r, c))
            answer.append(values[x][y])
        
    return answer

# commands = ["UPDATE 1 1 menu", "UPDATE 1 2 category", "UPDATE 2 1 bibimbap", "UPDATE 2 2 korean", "UPDATE 2 3 rice", "UPDATE 3 1 ramyeon", "UPDATE 3 2 korean", "UPDATE 3 3 noodle", "UPDATE 3 4 instant", "UPDATE 4 1 pasta", "UPDATE 4 2 italian", "UPDATE 4 3 noodle", "MERGE 1 2 1 3", "MERGE 1 3 1 4", "UPDATE korean hansik", "UPDATE 1 3 group", "UNMERGE 1 4", "PRINT 1 3", "PRINT 1 4"]
# print(solution(commands))
