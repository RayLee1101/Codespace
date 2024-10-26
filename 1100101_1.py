def fun1(length):
    for i in range(length):
        print(str(i + 1) * ( i + 1 ) + "#" * (length - 1 - i))
def fun2(length):
    string = ""
    for i in range(length):
        print(str("#" * (length - i - 1) * 2) + string + str(i + 1) + string[::-1])
        string = string + str(i + 1)
def fun3(length):
    string = ""
    array = []
    for i in range(length * 2):
        if i < length:
            string+=str(i+1)
            print(string + "^" * (length - i - 1))
            array.append(string[::-1])
        if i == length:
            array = array[::-1]
        if i >= length:
            print(array[i - length] + "^" * (i - length))
def fun4(length):
    string = "1";
    array = []
    for i in range(1, length * 2):
        if i <= length:
            array.append("^" * (length - i) + string + "^" * (length - i)) 
            print("^" * (length - i) + string + "^" * (length - i))
            string = str(i + 1) + string + str(i + 1)
        if i == length:
            array.pop()
            array = array[::-1]
        if i > length:
            print(array[i - length - 1])

def main():
    mode = int(input())
    length = int(input())
    if mode == 1:
        fun1(length)
    elif mode == 2:
        fun2(length)
    elif mode == 3:
        fun3(length)
    else:
        fun4(length)
main()