def main(n:int):
    result = []
    for i in range(n):
        string = string = "*" * (n - i - 1)
        list1 = [j for j in range((i+1)*2)if j % 2 == 1]
        list2 = list(reversed(list1))
        list2[0] = ""
        string += ''.join(map(str, list1)) + ''.join(map(str, list2))
        print(string)
        result.append(string)
    for i in range(len(result) - 1):
        print(result[len(result) - i - 2])
num = int(input())
if num > 0:
    main(num)
else:
    print("Error")