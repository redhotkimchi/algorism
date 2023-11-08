N , K = list(map(int, input().split()))
items = []

DP = [0 for _ in range(K+1)]

    
for _ in range(N):
    W, V = list(map(int, input().split()))
    items.append([W,V])

items = sorted(items, key = lambda x : x[0])

weight_list = []
for i in range(len(items)):
    W, V = items[i]
    DP[W] = max(V, DP[W])
    temp = []
    for weight in weight_list:
        if weight + W <= K:
            DP[weight + W] = max(DP[weight + W], DP[weight] + DP[W])
            temp.append(weight + W)
        else:
            break
    weight_list.append(W)
    weight_list = weight_list + temp
    weight_list = list(set(weight_list))
print(max(DP))

