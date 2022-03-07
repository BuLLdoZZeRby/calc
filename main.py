from num2words import num2words

# список доступных операторов
oper = ['+', '-', '*', '/']
# основной цикл. при вводе некорректной инфы выходим из цикла и шлем по пути русского военного корабля
while True:
    arg1 = input('Введите первый аргумент: ')
    if arg1[0] == "-":
        try:
            arg1 = int(arg1[1:]) * -1
        except:
            break
    else:
        try:
            arg1 = int(arg1)
        except:
            break
    operator = input('Выберете действие +, -, *, /')
    if operator not in oper:
        break
    arg2 = input('Введите второй аргумент: ')
    if arg2[0] == "-":
        try:
            arg2 = int(arg2[1:]) * -1
        except:
            break
    else:
        try:
            arg2 = int(arg2)
        except:
            break
    if operator == "+":
        result = arg1 + arg2
    elif operator == "-":
        result = arg1 - arg2
    elif operator == "*":
        result = arg1 * arg2
    else:
        if arg2 == 0:
            print('На ноль делить нельзя!')
            break
        else:
            result = arg1 / arg2
    print(f'Результат: {num2words(result, lang="ru")}')


print("Будь внимательнее. Попробуй еще раз!")