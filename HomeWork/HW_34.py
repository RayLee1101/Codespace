def prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return n != 1
def check(n):
    if n[0] != "A" or n[-1] != "G":
        return False
    if len(n) != 4:
        return False
    for i in range(1,3):
        if ord(n[i]) < 69 or ord(n[i]) > 84:
            return False
    return ord(n[1]) != ord(n[2])
def main():
    before = input()
    after = input().split()
    string = input().split(before)[1:]
    result = []
    for i in string:
        for j in after:
            if j in i and prime(len(i.split(j)[0])):
                result.append(i.split(j)[0])
                break
    if check(before) and len(result) > 0:
        for i in sorted(sorted(result), key=lambda x: len(x)):
            print(i)
    else:
        print("No gene")
main()