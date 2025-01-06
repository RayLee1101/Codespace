def create(string):
    data = []
    if len(string) == 5:
        data.append(string)
        return data
    for i in range(10):
        if str(i) not in string:
            data += create(string + str(i))
    return data

def new_arr(output, data, ans):
    new_data = []
    for i in data:
        if check(output, i) == ans:
            new_data.append(i)
    return new_data

def check(val1, val2):
    a, b = 0, 0
    for i in range(len(val1)):
        if val1[i] in val2:
            if i == val2.index(val1[i]):
                a += 1
            else:
                b += 1
    return f"{a}A{b}B"

def main(answer):
    data = create("")
    ans = check(data[0], answer)
    # ans = input(f"猜測：{data[0]}；結果：")
    while(ans != "5A0B"):
        data = new_arr(data[0], data, ans)
        ans = check(data[0], answer)
        # ans = input(f"猜測：{data[0]}；結果：")
    # print("End!")
    return data[0]

def test():
    print(main(input()))
test()