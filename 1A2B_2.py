import random
def create(string = ""):
    if len(string) == 4:
        return [string]
    data = []
    for i in range(10):
        if str(i) not in string:
            data += create(string + str(i))
    return data

def new_data(data, guess, request):
    return list(filter(lambda x: check(x, guess) == request , data))

def check(val1, val2):
    b = list(filter(lambda x: x in val2, val1))
    a = list(filter(lambda x: val1.index(x) == val2.index(x), b))
    return f"{len(a)}A{len(b)-len(a)}B"

def many_arr(data):
    re = ""
    # for i in range(4):
    #     dicts = {}
    #     for j in data:
    #         if j[i] in dicts:
    #             dicts[j[i]] += 1
    #         else:
    #             dicts[f"{j[i]}"] = 1
    #     # sorted(dicts.keys(), reversed = True)
    #     dicts = {key: dicts[key] for key in sorted(dicts.keys(), reverse=True)}
    #     for j in range(4):
    #         if list(dicts.keys())[j] not in re:
    #             re += list(dicts.keys())[j]
    #             break
    # return re
    for i in range(4):
        dicts = {}
        for j in data:
            if j[i] in dicts:
                dicts[j[i]] += 1
            else:
                dicts[j[i]] = 1
        for key in sorted(dicts.keys(), key=lambda k: dicts[k]):
            temp_re = re + key
            if any(item.startswith(temp_re) for item in data):
                re += key
                break
    return re

def main(num, answer):
    data = create()
    guess = data[0]
    # request = input(f"猜測：{guess}；結果：")
    request = check(guess, answer)
    num+=1
    # print(f"猜測{num}次：{guess}；結果：{request}")
    while(request != "4A0B" and request != "4A"):
        # print(guess)
        data = new_data(data, guess, request)
        # guess = many_arr(data)
        # print(guess)
        guess = data[0]
        request = check(guess, answer)
        num+=1
        # print(f"猜測{num}次：{guess}；結果：{request}")
        # request = input(f"猜測：{guess}；結果：")
    # print("END！")
    # return num
    return guess
def test():
    print(main(0, int(input())))
    # data = create()
    # _max = 0
    # _min = 1000000
    # total = 0
    # for i in data:
    #     n = main(0, i)
    #     total += n
    #     _max = max(_max, n)
    #     _min = min(_min, n)
    # print(_max)
    # print(_min)
    # print(total / len(data))
test()