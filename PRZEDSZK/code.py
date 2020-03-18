def nwd(a, b): 
    return nwd(b, a%b) if b else a

def nww(a, b): 
    return a*b//nwd(a, b)

n = int(input())
for i in range(n):
    inpt = input().split()
    a,b = int(inpt[0]), int(inpt[1])
    print(nww(a,b))