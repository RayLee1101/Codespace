def request(M, n):
    if n == 0 or n == 1:
        return 0
    elif(n % 2 == 1):
        n += 1
    return request(M, n // 2) + 1
def main():
    M = input()
    result = []
    while(M != "-1"):
        num = 0
        result.append(request(M, int(M,2)))
        M = input()
    for i in result:
        print(f"{i:04b}")
main()