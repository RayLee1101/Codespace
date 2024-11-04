def check(card):
    num = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
    arr = [ j+i for j in num for i in ["S", "H", "D", "C"] ]
    if len(list(filter(lambda x: x not in arr, card))) != 0:
        return "Error"
    return card

def number(card):
    number = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
    num = sorted([number.index(i[:-1]) for i in card])
    num_diff = [num[i] - num[i - 1] for i in range(1, 5)]
    if len(set(num)) == 5:
        if len(set(i[-1] for i in card)) == 1 and set(num_diff) <= set([1, 9]):
            return 9
        elif len(set(i[-1] for i in card)) == 1:
            return 6
        elif set(num_diff) <= set([1, 9]):
            return 5
        return 1        
    elif len(set(num)) == 4:
        return 2
    elif len(set(num)) == 3:
        if True in [num[i] == num[i - 1] == num[i - 2] for i in range(2, 5)]:
            return 4
        return 3
    if True in [num[i] == num[i - 1] == num[i - 2]  == num[i - 3] for i in range(3, 5)]:
        return 8
    return 7

def main():
    card1 = check(list(set(input().split())))
    card2 = check(list(set(input().split())))
    if card1 == "Error" or card2 == "Error":
        print("Error input")
    elif len(card1) < 5 or len(card2) < 5 or len(set(card1+card2)) < 10:
        print("Duplicate deal")
    else:
        print(max(number(card1), number(card2)))
main()