list = list(map(int, input("").split()))
ans = []
for i in range(len(list) - 1):
    ans.append(list[i] + list[i + 1])
print(ans)