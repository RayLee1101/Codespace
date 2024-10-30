def check(x, cla):
    global state
    for i in range(len(state)):
        if state[i][1] == x:
            conflict.append([min(state[i][0], cla), max(state[i][0], cla), x])
        if state[i][2] == x:
            conflict.append([min(state[i][0], cla), max(state[i][0], cla), x])
conflict = []
state = []
for i in range(3):
    classID = int(input())
    classtime1 = int(input())
    classtime2 = int(input())
    check(min(classtime1, classtime2), classID)
    check(max(classtime1, classtime2), classID)
    state.append([classID, classtime1, classtime2])
# print(conflict)
conflict.sort(key=lambda x: x[2])
conflict.sort(key=lambda x: x[1])
conflict.sort(key=lambda x: x[0])
if len(conflict) == 0:
    print("correct")
else:
    for i in range(len(conflict)):
        print("%d and %d conflict on %d" % (int(conflict[i][0]), int(conflict[i][1]), int(conflict[i][2])))