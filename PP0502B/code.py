n = int(input())
for i in range(n):
    lst = input().split()[1:]
    lst.reverse()
    print(" ".join(lst))