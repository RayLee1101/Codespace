lists = list(map(lambda x: int(x), input().split()))
total = int(input())
max = 0
result = []
for i in range (len(lists)):
    for j in range(i, len(lists)):
        if lists[i] + lists[j] == total and i * j > max:
            result = [i, j]
            max = i*j
print(list(sorted(result, reverse=True)))