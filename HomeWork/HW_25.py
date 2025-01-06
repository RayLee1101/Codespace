def search(string, d):
    stack = []
    dicts = []
    left = ["{", "[", "("]
    right = ["}", "]", ")"]
    for i in string:
        if i in left:
            stack.append(i)
        elif i in right:
            if len(stack) > 0 and right[left.index(stack[-1])] == i:
                stack.pop()
            else:
                return "fail"
        else:
            dicts.append([i, len(stack)])
    if len(stack) != 0:
        return "fail"
    data = list(map(lambda x:x[0] ,filter(lambda x: x[1] == d, dicts)))
    if len(data) == 0:
        return "pass,EMPTY"
    else:
        return "pass," + "".join(data)

def main():
    n = int(input())
    d = int(input())
    for i in range(n):
        print(search(input(), d))
main()