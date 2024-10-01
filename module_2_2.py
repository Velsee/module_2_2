print('Ввод в консоль:')
first = int(input())
second = int(input())
third = int(input())

if first == second == third:
    print('\n' 'Вывод на консоль:', 3, sep="\n")
elif first == second or first == third or second == third:
    print('\n' 'Вывод на консоль:', 2, sep="\n")
else:
    print('\n' 'Вывод на консоль:', 0, sep="\n")