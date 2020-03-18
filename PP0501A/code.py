def nwd(a, b): 
    return nwd(b, a%b) if b else a
    
n = int(input())
for i in range(n):
    a,b = list(map(int, input().split()))
    print(nwd(a,b))