word = list(map(str, input()))
answer = 1
before = word[0]
for i in range(1, len(word)):
    if word[i] > before:
        before = word[i]
    else:
        answer += 1
        before = word[i]
print(answer)
