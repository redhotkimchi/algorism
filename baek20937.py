from collections import Counter
N = int(input())
numbers = list(map(int, input().split()))
numbers.sort(reverse = True)
count = Counter(numbers).most_common()

print(count[0][1])