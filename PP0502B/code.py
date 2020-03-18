def reverse(lst):
    for i in range(len(lst)//2):
        lst[i],lst[len(lst)-i-1] = lst[len(lst)-i-1],lst[i]
    return " ".join(lst)
        
n = int(input())
for i in range(n):
    lst = list(input().split())[1:]
    print(reverse(lst))