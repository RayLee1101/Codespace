N = int(input())
if N % 2 != 0:
    for i in range(N):
        string = ""
        for j in range(N - i - 1):
            string += "#"
        for j in range((i) * 2 + 1):
            string += "*"
        print(string)
else:
    for i in range(N):
        string = ""
        for j in range(N):
            if(i == 0 or i == N - 1 or j == 0 or j == N - 1):
                string += "*"
            else:
                string += "#"
        print(string)