import math
import copy
def eigenvalues(arr):
    a = 1
    b = -(arr[0][0] + arr[1][1])
    c = arr[0][0] * arr[1][1] - arr[0][1] * arr[1][0]
    if b*b-4*a*c < 0:
        return "Not real number"
    ans1 =  int((-b+(math.sqrt(b*b-4*a*c))) / (2*a))
    ans2 =  int((-b-(math.sqrt(b*b-4*a*c))) / (2*a))
    return [ans1, ans2]
def eigenvectors(arr):
    if arr == [[0,0],[0,0]]:
        return "Any non-zero vector"
    b = arr[0][0] - arr[1][0]
    a = -arr[0][1] + arr[1][1]
    _hcf = hcf(abs(a),abs(b))
    if a < 0 and b < 0:
        a = -a
        b = -b
    return [int(a / _hcf), int(b / _hcf)]

def hcf(a,b):
    _max = 1
    for i in range(2, min(a,b) + 1):
        if a % i == 0 and b % i == 0:
            _max = i
    return _max    

def main():
    A = [[1,6],[5,2]]
    B = [[2,3],[3,-6]]
    C = [[7,2],[-4,1]]
    X = [[1,1],[-1,1]]
    Z = [[0,0],[0,0]]
    for i in [A,B,C,X,Z]:
        print(i)
        evalue = eigenvalues(i)
        print(f"eigenvalues:{evalue}")
        if evalue == "Not real number":
            continue
        for j in evalue:
            arr = copy.deepcopy(i)
            arr[0][0] -= j
            arr[1][1] -= j
            print(f"{j};eigenvectirs:{eigenvectors(arr)}")
main()