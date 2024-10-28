lists = list(map(lambda x: int(x), input().split()))
total = int(input())
max = -1
result = []
for i in range (len(lists)-1):
    for j in range(i+1, len(lists)):
        if lists[i] + lists[j] == total and i * j > max:
            result = [i, j]
            max = i*j
print(list(sorted(result, reverse=True)))