def change_matrix(array, m):
    if m < 0 or m > 2:
        return ["ERROR"]
    if m == 1:
        array = array[::-1]
    if m == 2:
        n = len(array)
        arr = [[i * n + j for j in range(n)] for i in range(n)]
        for i in range(n):
            for j in range(n):
                arr[i][n - j - 1] = array[j][i]    
        array = arr
    return array

def main():
    n = int(input())
    if 1 <= n and n <= 10:
        array = [[i * n + j for j in range(n)] for i in range(n)]
        result = []
        m = int(input())
        while(m != -1):
            result += change_matrix(array, m)
            m = int(input())
        for i in result:
            if i != "ERROR":
                print("".join(f"{x:3d}" for x in i))
            else:
                print(i)
        # for i in result:
        #     if i != "ERROR":
        #         for j in i:
        #             print(*j, sep="   ")
        #     else:
        #         print(i)
    else:
        print("ERROR")
main()