list = list(map(int, input("").split()))
ans = []
for i in range(len(list)):
    state = list[i] != 1
    for j in range(2, list[i] - 1):
        if list[i] % j == 0:
            state = False
    if state:
        ans.append(list[i])
if len(ans) >= 1:
    ans.sort()
    print(ans)
else:
    print("No prime number")