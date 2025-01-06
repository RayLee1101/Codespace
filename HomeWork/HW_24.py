def search(arr):
    num = set(["1", "2", "3", "4"])
    for i in range(4):
        for j in range(4):
            if arr[i][j] != "0":
                continue
            x = i - (i % 2)
            y = j - (j % 2)
            for k in range(x, x + 2):
                for l in range(y, y + 2):
                    num -= {arr[k][l]}
            num -= set(arr[i])
            num -= set(map(lambda x: x[j], arr))
            if len(num) == 1:
                arr[i][j] = list(num)[0]
        num = set(["1", "2", "3", "4"])
    return arr
def main():
    arr = [ input().split() for _ in range(4)]
    d = list(filter(lambda x: "0" in x, arr))
    while(len(d) != 0):
        arr = search(arr)
        d = list(filter(lambda x: "0" in x, arr))
    for i in arr:
        print(" ".join(i))
main()