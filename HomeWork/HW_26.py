def combination(arr, n):
    result = []
    arr2 = arr.copy()
    for i in arr:
        if i[0] <= n:
            n -= i[0]
            result.append(i)
            arr2.remove(i)
        if n == 0:
            break
    return arr2, result
def main():
    goods = list(map(lambda x: (int(x[0: -1]), x[-1]),input().split()))
    _max = int(input())
    if _max > 10 or _max < 1:
        print("Input Error")
        return
    if len(list(set(goods))) != len(goods):
        print("Duplicated ID")
        return
    for i in goods:
        if i[0] > _max:
            print("Load limit exceeded")
            return
    result = []
    while( len(goods) > 0):
        goods, res = combination(goods, _max)
        result.append(sorted(list(map(lambda x: x[1], res))))
        if sum(list(map(lambda x: x[0], res))) != _max:
            print("Cannot be delivered")
            return
    result = sorted(result)
    print(len(result))
    for i in list(sorted(result, key= lambda x: len(x))):
        print(" ".join(i))
main()