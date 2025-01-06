def reset(data):
    dicts = {}
    for item in data:
        if item[1] in dicts:
            dicts[item[1]] += 1
        else:
            dicts[item[1]] = 1
    return [item for item in data if dicts[item[1]] == 1]

card = [reset(input().split()), reset(input().split()), reset(input().split())]
extract = [input(), input(), input()]
try:
    for i in range(3):
        card[i].append(extract[i])
        card[i] = reset(card[i])
        card[(i + 1) % 3].remove(extract[i])
    for i in card:
        print(" ".join(i))
except ValueError:
    print("Error")

