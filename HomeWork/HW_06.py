state = [0, 0, 0]
date183 = [0.08, 0.1393,0.1349,1.1287,1.4803]
date383 = [0.07, 0.1304,0.1217,1.1127,1.2458]
date983 = [0.06, 0.1087,0.1018,0.9572,1.1243]
for i in range(5):
    s = int(input(""))
    state[0]+= s*date183[i]
    state[1]+= s*date383[i]
    state[2]+= s*date983[i]
if state[0] < 183:
    state[0] = 183
if state[1] < 383:
    state[1] = 383
if state[2] < 983:
    state[2] = 983


if state[0] < min(state[1], state[2]):
    print(int(state[0]))
    print("183")
if state[1] < min(state[0], state[2]):
    print(int(state[1]))
    print("383")
if state[2] < min(state[1], state[0]):
    print(int(state[2]))
    print("983")