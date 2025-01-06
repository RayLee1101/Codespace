def Combination(s):
    if len(s) == 1:
        return [s]
    data = []
    for i in range(len(s)):
        for j in Combination(s[:i] + s[i+1:]):
            data.append(s[i] + j)
    return data
def main():
    data = Combination("".join(input().split()))
    data = sorted([int(i, 16) for i in data])
    num = data[0] + data[-1]
    if len(data) % 2 == 0:
        num += (data[len(data) // 2 - 1] + data[len(data) // 2]) // 2 
    else:
        num += data[len(data) // 2]
    while(num >= 10):
        num = sum([int(i) for i in str(num)])
    print(num)
main()