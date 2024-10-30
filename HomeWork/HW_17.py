def fish(n, m):
    array = []
    for i in range(n):
        string = "_" * (n-i-1) + "*" * (i * 2 + 1) + "_" * (n-i-1) + "_" * (n-i-1) + "*" * (i * 1 + 1)
        if m % 2 == 1:
            array.append(string)
        else:
            array.append(string[::-1])
    for i in array:
        print(i)
    array.pop()
    for i in array[::-1]:
        print(i)

def trianle(n, m):
    string = "1"
    array = []
    for i in range(n):
        array.append("_" * (n - i - 1) + string + "_" * (n - i - 1))
        string = str(i+2) + string + str(i+2)
    if m % 2== 0:
        array = array[::-1]
    for i in array:
        print(i)

def main():
    n = int(input())
    m = int(input())
    c = int(input())
    if c == 1:
        fish(n, m)
    else:
        trianle(n, m)

main()