def happy(n):
    num = []
    while(n != 1 and n not in num):
        num.append(n)
        n = sum([pow(int(i), 2) for i in str(n)])
    return n == 1

def love(n):
    length = len(str(n))
    num = sum([pow(int(i), length) for i in str(n)])
    return n == num

def F(n):
    if n == 1 or n == 2:
        return 1
    else:
        return F(n - 1) + F(n - 2)

def main():
    num = int(input())
    h = happy(num)
    l = love(num)
    n = num
    while(n > 10):
        n = sum([int(i) for i in str(n)])
    if h and l:
        print(f"{num} is both a happy number and a narcissistic number.")
        print(f"F({n}) = {F(n)}")
    elif h:
        print(f"{num} is a happy number.")
        print(f"F({n}) = {F(n)}")
    elif l:
        print(f"{num} is a narcissistic number.")
        s = 1
        for i in range(1, n + 1):
            s *= i
        print(f"{n}! = {s}")
    else:
        print(f"{num} is neither a happy number nor a narcissistic number.")
        s = 1
        for i in range(1, n + 1):
            s *= i
        print(f"{n}! = {s}")
main()