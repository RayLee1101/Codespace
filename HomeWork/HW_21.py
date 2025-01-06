def main():
    n = int(input())
    m = int(input())
    a = [int(input())]
    b = float(input())
    c = int(input())
    d = float(input())
    c2 = 0
    total = 0
    for i in range(m):
        total += a[-1]
        print(" ".join(map(str, [i+1, sum(a), a[-1], c2])))
        x = (b / c) * (1 - d)
        y = min( int((1-d) * n- sum(a)), int(sum(a) * x))
        y = max(0, y)
        a.append(y)
        if len(a) > c:
            c2 = a[0]
            d = (n * d + a[0]) / n
            a.pop(0)
    print(total)
main()