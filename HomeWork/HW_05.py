trian = []
trian.append(int(input()))
trian.append(int(input()))
trian.append(int(input()))
trian.sort()
if trian[0] == trian[2]:
    print("Equilateral Triangle")
if sum(trian) / 2 >= trian[2]:
    if trian[0] == trian[1] or trian[1] == trian[2]:
        print("Isosceles Triangle")
    if trian[0] * trian[0] + trian[1] * trian[1] < trian[2] * trian[2]:
        print("Obtuse Triangle")
    if trian[0] * trian[0] + trian[1] * trian[1] == trian[2] * trian[2]:
        print("Right Triangle")
    if trian[0] * trian[0] + trian[1] * trian[1] > trian[2] * trian[2]:
        print("Acute Triangle")
else:
    print("Not Triangle")