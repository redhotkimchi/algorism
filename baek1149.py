N = input()
house_list = []
Min_Value = float("inf")

DP = [[float("inf") for x in range(3)]for _ in range(int(N))]

for _ in range(int(N)):
    Red, Green, Blue = map(int, input().split())
    house_list.append([Red, Green, Blue])

DP[0] = [house_list[0][0],house_list[0][1],house_list[0][2]]
for i in range(1, int(N)):
    DP[i][0] = min(house_list[i][0]+DP[i-1][1],house_list[i][0]+ DP[i-1][2])
    DP[i][1] = min(house_list[i][1]+DP[i-1][0],house_list[i][1]+ DP[i-1][2])
    DP[i][2] = min(house_list[i][2]+DP[i-1][0],house_list[i][2]+ DP[i-1][1])
print(min(DP[int(N)-1]))
