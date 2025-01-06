def check(data):
    state = True
    if len(data[0]) != 3 or "I" in data[0] or "O" in data[0]:
        state = False
    if len(data[1]) != 4 or "4" in data[1]:
        state = False
    for i in data[0]:
        if ord(i) < 65 or ord(i) > 90:
            state = False
    for i in data[1]:
        if ord(i) < 48 or ord(i) > 57:
            state = False
    return state

def main(data):
    state = check(data)
    d = ["FUC","FUG","FUQ","FUT","GPU","KGB","KGB","KMT","DPP","PUG","PUP","CAT","ANT","APE","MAD","NUN","SEX","SLY","BAD","GAY","ASS","BUM","BRA","CRY"]
    if data[0] in d:
        state = False
    if state:
        print(f"{data[0]}-{data[1]} is Valid license plate number.")
    else:
        print(f"{data[0]}-{data[1]} is Invalid license plate number.")
main(input().split("-"))