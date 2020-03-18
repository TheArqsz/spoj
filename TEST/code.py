def is_palindrome(n):
    str_n = str(n)
    for i in range(int(len(str_n)/2) + 1):
        if str_n[i] == str_n[len(str_n) - i - 1]:
            continue
        else:
            return False
    return True

def get_reversed(n):
    return int(str(n)[::-1])
    
amnt = int(input())
for t in range(amnt):
    numb = int(input())
    how_many_adding = 0
    while not is_palindrome(numb):
        how_many_adding += 1
        numb += get_reversed(numb)
    print(f"{numb} {how_many_adding}")