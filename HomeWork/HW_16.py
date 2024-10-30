number = ['A','2','3','4','5','6','7','8','9','T','J','Q','K']
color = ['S', 'H', 'D', 'C']
def card_check(data):
    state = True
    for x in data:
        if x[0] == '1' and x[1] =='0' and len(x) == 3:
            if x[2] not in color:
                state = False
        elif x[0] not in number or x[1] not in color or len(x) != 2 and x[0] != 'T':
            state = False
    return state

def card_number(data):
    data = list(map( lambda x: x.replace('A', 'T').replace('1', 'A').replace('B','J').replace('C','Q').replace('D','K'), data))
    level = 1
    repart = []
    for i in data:
        state = True
        for j in repart:
            if i[0] == j[0]:
                j[1]+=1
                state = False
        if state:
            repart.append([i[0], 1])
    max_repart = list(map(lambda x: x[1],filter(lambda x:x[1] > 1 , repart))) # 8 7 4 3 2
    max_repart = sorted(max_repart, reverse=True)
    if len(max_repart) >= 1:
        if max_repart[0] == 4:
            level = max(level, 8)
        if max_repart[0] == 3:
            if len(max_repart) == 2 and max_repart[1] == 2:
                level = max(level, 7)
            level = max(level, 4)
        if max_repart[0] == 2:
            if len(max_repart) == 2:
                level = max(level, 3)
            else:
                level = max(level, 2)
    
    for j in range(5):
        state = True
        for i in range(len(data) - 1):
            if number[(number.index(data[(i + j)%5][0]) + 1) % 13] != data[(i + 1 + j) % 5][0]:
                state = False
                continue
        if state:
            level = max(level, 5)
            break
       
    state = True
    for i in range(len(data) - 1):
        if data[i][1] != data[i + 1][1]:
            state = False
    if state:
        if level == 5:
            level = 9
        else:
            level = 6
    return level

def main():
    data = list(set(input().split()))
    if card_check(data):
        if len(data) == 5:
            print(card_number( sorted( list( map( lambda x: x.replace('A', '1').replace('10', 'A').replace('J','B').replace('Q','C').replace('K','D'), data) ) ) ) )
        else:
            print("Duplicate deal")
    else:
        print("Error input")
main()