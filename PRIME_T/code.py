import math
n = int(input())
for i in range(0, n):
    numb = int(input())
    if numb < 2 or (not numb & 0x1 and numb> 2): 
        print("NIE")
    elif all(numb % ii for ii in range(3, int(math.sqrt(numb)) + 1, 2)):
        print("TAK")
    else:
        print("NIE")