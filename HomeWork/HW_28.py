def line(arr, size):
    state = 0
    great = [True for i in range(size)]
    for _ in range(2):
        for i in arr:
            if i == great:
                state += 1
        arr =[[arr[j][i] for j in range(size)] for i in range(size)]
    for _ in range(2):
        s = True
        for i in range(size):
            if arr[i][i] != True:
                s = False
        if s:
            state += 1
        arr = [i[::-1] for i in arr]
    return state
def main():
    size = int(input())
    answer = int(input())
    inp = input().split()
    arr1 = [inp[i:i+size] for i in range(0, size * size, size)]
    inp = input().split()
    arr2 = [inp[i:i+size] for i in range(0, size * size, size)]
    answer = input().split()
    for i in [arr1, arr2]:
        for k in i:
            for l in set(answer).intersection(set(k)):
                k[k.index(l)] = True
    line1 = line(arr1, size)
    line2 = line(arr2, size)
    if line1 > line2:
        print("A Win")
    elif line2 > line1:
        print("B Win")
    else:
        print("Tie")
main()