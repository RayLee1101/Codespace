def input_data():
    n = int(input())
    course = []
    for i in range(n):
        course.append([int(input()),[]])
        for j in range(int(input())):
            course[i][1].append(int(input("time:")))
    check_conflict(n, course)

def check_conflict(n, course):
    for i in range(n-1):
        for j in range(i + 1, n):
            check(course[i], course[j])
  #          for x in range(len(course[x][1])):
        #        if course[i][1][x] in course[j][1]:
           #         print(f"{course[i][0]} and {course[j][0]} conflict on {course[i][1][x]}")
def check(val1, val2):
    for x in range(len(val1[1])):
        if val1[1][x] in val2[1]:
            print(f"{val1[0]} and {val2[0]} onflict on {val1[1][x]}")
def main():
    input_data()

main()