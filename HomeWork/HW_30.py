def main():
    num = int(input())
    school = []
    for _ in range(num):
        school.append(input().split())
    condition = []
    num = int(input())
    for _ in range(num):
        condition.append([i.split() for i in input().split("+")])
    state = input()
    result = []
    if state == "0":
        for cond in condition:
            r = []
            for s in school:
                for c in cond:
                    if all(item in s for item in c) and s[0] not in r:
                        r.append(s[0])
            result.append(r)
    else:
        for cond in condition:
            r = []
            for s in school:
                su = 0
                for c in cond:
                    su += sum(1 for item in c if item in s)
                r.append([s[0], su])
            r = sorted(r, key = lambda x: x[1], reverse=True)
            result.append(list(map(lambda x: x[0], filter(lambda x: x[1] == r[0][1], r))))
    for i in result:
        print(" ".join(i))
main()