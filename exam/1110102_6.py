length, start = map(int, input().split(" "))
mymap = []
for i in range(length):
    mymap.append(list(map(int, input().split(" "))))
max_sum = 0
def dfs(router, sum, mm):
    global max_sum, res
    if len(router) == length or mm[0] in router:
        if sum > max_sum:
            max_sum = sum
    else:
        router.append(mm[0])
        if mm[2] != 0:
            next_list = list(filter(lambda x: x[0] == mm[2], mymap))[0]
            dfs(router.copy(), sum + mm[1], next_list)
        if mm[3] != 0:
            next_list = list(filter(lambda x: x[0] == mm[3], mymap))[0]
            dfs(router.copy(), sum + mm[1], next_list)
        if mm[2] == 0 and mm[3] == 0 and sum > max_sum:
            max_sum = sum
next_list = list(filter(lambda x: x[0] == start, mymap))[0]
dfs( [], 0,  next_list)
print(max_sum)