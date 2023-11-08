N,M,K = list(map(int, input().split()))

num_list = []
for _ in range(N):
    num_list.append(int(input()))

for _ in range(M + K):
    a , b, c = list(map(int,input().split()))

tree = [0] * (len(num_list) *4)
def init(start, end, index, tree):
    
