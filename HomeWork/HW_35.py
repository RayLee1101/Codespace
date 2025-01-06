def check_id(s):
    dicts = "ABCDEFGHJKLMNPQRSTUVXYWZIO"
    if s[0] not in dicts:
        return "Wrong area code"
    if s[1] != "1" and s[1] != "2":
        return "Wrong gender code"
    s = str(dicts.index(s[0]) + 10) + s[1:]
    n = int(s[0])
    for i in range(9):
        n += int(s[i + 1]) * (9-i)
    num = 10 - n % 10
    if num == 10:
        num = 0
    if num != int(s[-1]):
        return "Illegal"
    return "Pass" 

def check_pw(n):
    num = 0
    for i in range(len(n)):
        if ord(n[i]) >= 65 and ord(n[i]) <= 90:
            num += 3
        elif ord(n[i]) >= 97 and ord(n[i]) <= 122:
            num += 1
        elif ord(n[i]) >= 48 and ord(n[i]) <= 57:
            num += 2
        elif n[i] in "~!@#$%^&*<>_+=":
            num += 5
    n_num = 0
    n = "b" + n + "b"
    for i in range(1, len(n)-1):
        if ord(n[i]) >= 48 and ord(n[i]) <= 57 and not(ord(n[i-1]) >= 48 and ord(n[i-1]) <= 57) and  not(ord(n[i+1]) >= 48 and ord(n[i+1]) <= 57):
            n_num+=1
    if n_num >= 5:
        num += 15
    if num >= 30:
        return num
    else:
        return f"{num} Not strong enough"
def main():
    Id = check_id(input())
    pw = check_pw(input())
    print(Id)
    print(pw)
main()
