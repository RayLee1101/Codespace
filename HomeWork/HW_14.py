def check (val1:list, val2:list):
    for i in range(len(val1) - 1):
        for j in range(len(val2) - 1):
            if val1[i + 1] == val2[j + 1]:
                result.append([val1[0], val2[0], val1[i + 1]])
def name_check(name):
    try:
        test = int(name[-4:])
    except ValueError:
        state = False
num = int(input())
data = []
result = []
state = True
if num < 2 or num > 10:
    state = False
for i in range(num):
    _data = [input()]
    name_check(_data[0])
    class_num = int(input())
    if class_num >= 1 and class_num <= 3:
        for j in range(class_num):
            class_time = input()
            if class_time[0] not in ['1','2','3','4','5'] or class_time[1] not in ['1','2','3','4','5','6','7','8','9','a','b','c']:
                state = False 
            _data.append(class_time)
        data.append(_data)                    
    else:
        state = False
if state:
    for i in range(len(data)):
            for j in range(len(data) - i - 1):
                check(data[i], data[i + j + 1])
    if len(result) == 0:
        print("correct")
    else:
        for i in range(len(result)):
            print(",".join(result[i]))
else:
    print("-1")