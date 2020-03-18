ile = int(input())
for i in range(0, ile):
    wyraz = input() + '#'
    wyraz_lst = list(wyraz)
    last_char = wyraz_lst[0]
    last_char_amnt = 1
    final_word = ''
    for i in range(1,len(wyraz_lst)):
        if wyraz_lst[i] == wyraz_lst[i-1]:
            last_char_amnt += 1
            last_char = wyraz_lst[i]
        else:
            if last_char_amnt > 2:
                final_word += last_char + str(last_char_amnt)
            else:
                final_word += last_char*last_char_amnt
            last_char = wyraz_lst[i]
            last_char_amnt = 1
    print(final_word)