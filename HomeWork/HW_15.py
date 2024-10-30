def check(string: str):
    for i in range(len(string)):
        try:
            num = int(string[i])
            data.append(num)
        except ValueError:
            continue
data = []
reply = []
check(input())
if list(reversed(data)) == data:
    data.sort()
    print(list(set(data)))
else:
    for i in range(len(data)):
        state = True
        for j in range(len(reply)):
            if data[i] == reply[j][0]:
                reply[j][1]+=1
                state = False
        if state:
            reply.append([data[i], 1])
    result = list(filter(lambda x: x is not None, map(lambda x:x[0] if x[1] > 1 else None ,reply)))
    result = sorted(result, reverse=True)
    print(result)