def is_int(x):
    return  (x - int(x)) == 0

arr = [0,0]
for i in range(2):
    for j in range(3):
        str = input("")
        if str.isdigit():
            arr[i] += int(str)
        elif str == "A":
            arr[i] += 1
        else:
            arr[i] += 0.5
if is_int(arr[0]):
    arr[0] = int(arr[0])
if is_int(arr[1]):
    arr[1] = int(arr[1])
if arr[0] > 10.5:
    arr[0] = 0
if arr[1] > 10.5:
    arr[1] = 0
print(arr[0])
print(arr[1])
if arr[0] > arr[1]:
    print("X Win")
elif arr[0] == arr[1]:
    print("Tie")
else:
    print("Y Win")