def Combination(s):
    if len(s) == 1:
        return [s]
    data = []
    for i in range(len(s)):
        for j in Combination(s[:i] + s[i+1:]):
            data.append(s[i] + j)
    return data
def main():
    string = input()
    num = int(input())
    arr = Combination(string)
    print(", ".join(arr))
    arr = [i[0:num] for i in arr]
    arr2 = []
    for i in arr:
        if set(i) not in list(map(lambda x: set(list(x)), arr2)):
            arr2.append(i)
    # for i in arr:
    #     if set(i) not in list(map(lambda x: set(x), arr2)):
    #         arr2.append(i)
    print(", ".join(list(map(lambda x: "".join(list(x)), arr2))))
main()