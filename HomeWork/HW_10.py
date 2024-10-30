point = [] #每球的分數
for i in range(3): #跑3局
    num = int(input())
    point.append(num) #將第一球的分數加進
    if num != 10: #不是全倒 表示還有第二球
        num = int(input())
        point.append(num) #將第二球的分數加進
        if num + point[-2] == 10 and i == 2: #第一加第二球有沒有10 並且如果是最後一局需要往後多一球
            num = int(input())
            point.append(num)
    elif num == 10 and i == 2: #如果全倒 並且是最後一局
        for j in range(2):#額外多兩球
            num = int(input())
            point.append(num)

bureau = 0 #紀錄局數
run = 0 #當局第幾球
result = 0 #總分
for i in range(len(point)):
    result+=point[i] #將分數加入總分
    if point[i] == 10 and bureau < 3: #如果是全倒額外加兩球
        result+=point[i+1]
        result+=point[i+2]
        bureau+=1
    else:
        run+=1
        if run == 2: #若是當局第二球
            if point[i] + point[i-1] == 10:
                result+=point[i+1]
            bureau+=1
            run = 0
    if bureau == 3: #表示每一局都跑完了
        print(result)
        bureau+=1 #防止重複執行