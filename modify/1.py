def input_data():
    n = int(input())
    course = [[] for _ in range(n)]
    for i in range(n):
        course[i].append(int(input()))
        time = int(input())
        course[i].append(time)
        for j in range(time):
            course[i].append(int(input()))
    print(course)
    return n, course
            
def check_conflict(n, course):
    conflict = []
    for i in range(n-1):
        for j in range(i+1,n):
            for x in range(course[i][1]):
                for y in range(course[j][1]):
                    if course[i][x+2] == course[j][y+2]:
                        conflict.append(course[i][0])
                        conflict.append(course[j][0])
                        conflict.append(course[i][x+2])
    print(("{} and {} conflict on {}").format(conflict[0],conflict[1],conflict[2]))

def main():
    n, course = input_data()
    check_conflict(n, course)

main()