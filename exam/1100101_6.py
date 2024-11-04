def getcard(arr, dict, mode = False, Other = []):
    state = input().split()
    while(state[0] == "Y" and sum(arr) < 10.5 and len(arr) < 5):
        arr.append(dict[state[1]])
        if sum(arr) < 10.5 and len(arr) < 5:
            state = input().split()
    return arr

def computer_getcard(arr, dict, Other):
    Other_number = list(map(lambda x: sum(x), filter(lambda x: len(x) < 5 and x != arr and sum(x) < 10.5,Other)))
    if Other_number != []:
        while(min(Other_number) > sum(arr)):
            arr.append(dict[input()])
    return arr

def main():
    dict = {"A": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10, "J": 0.5, "Q": 0.5, "K": 0.5}
    num = int(input())
    price = list(map(int, input().split()))
    player = list(map(lambda x :[ dict[x]], input().split()))
    for i in range(1, len(player)):
        player[i] = getcard(player[i], dict)
    player[0] = computer_getcard(player[0], dict, player)
    for i in range(1, len(player)):
        if sum(player[i]) > 10.5:
            print(f"Player{i} -{price[i-1]}")
        elif sum(player[0]) > 10.5:
            print(f"Player{i} +{price[i-1]}")
        elif sum(player[i]) == 10.5:
            print(f"Player{i} +{price[i-1]}")
        elif len(player[i]) == 5:
            print(f"Player{i} +{price[i-1]}")
        elif sum(player[0]) >= sum(player[i]):
            print(f"Player{i} -{price[i-1]}")
        else:
            print(f"Player{i} +{price[i-1]}")

main()