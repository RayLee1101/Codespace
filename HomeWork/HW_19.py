def change_point(array, list1, level):
    for i in range(len(list1)):
        if list1[i] == "1":
            array = add_point(array, level, i)
    return array

def add_point(array, i, j):
    for x in range(i - 1, i + 2):
        for y in range(j - 1, j + 2):
            if x == i and y == j:
                array[x][y][0] = 0
                array[x][y][1] = False
            elif x >= 0 and y >= 0 and x < len(array) and y < len(array) and array[x][y][1]:
                array[x][y][0] += 1
    return array

def main():
    n = int(input())
    array = [ [ [0, True] for i in range(n) ] for i in range(n)]
    for i in range(n):
        array = change_point(array, input().split(" "), i)
    for i in array:
        for j in i:
            print(j[0], end=" ")
        print()
main()