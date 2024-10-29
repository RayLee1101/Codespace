def input_data():
    course = []
    for i in range(int(input())):
        course.append([int(input()),[]])
        for j in range(int(input())):
            course[i][1].append(int(input("time:")))
    check_conflict(len(course), course)

def check_conflict(n, course):
    for i in range(n-1):
        for j in range(i + 1, n):
            check(course[i], course[j])

def check(val1, val2):
    for x in range(len(val1[1])):
        if val1[1][x] in val2[1]:
            print(f"{val1[0]} and {val2[0]} onflict on {val1[1][x]}")
            
def main():
    input_data()

main()