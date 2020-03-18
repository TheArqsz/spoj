ile = int(input())
for i in range(0, ile):
    podstawa, wykladnik = input().split()
    if (int(wykladnik) - 1) % 4:
        print((int(podstawa) ** (((int(wykladnik)-1) % 4) + 1)) % 10)
    else:
        print(podstawa)