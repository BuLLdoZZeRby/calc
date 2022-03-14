try:
    from num2words import num2words
    num = True
except ModuleNotFoundError:
    num = False
    print("Отсутствует модуль num2words. Для корректной работы выполните команду: pip install num2words")


oper = ['+', '-', '*', '/']     # список доступных операторов
count_cycle = 0     # переменная количества циклов
# основной цикл.
while True:
    arg1 = input('Введите первый аргумент (или "стоп" для завершения): ')   # вводим первый аргумент
    if arg1.lower() == "стоп" or arg1.lower() == "stop":    # проверяем стоп слово,
        print('Hasta la vista...')                          # оно может быть написано в любом регистре
        break
    else:
        try:
            arg1 = float(arg1)                # пробум перевести строку во float, если не получается попускаем итерацию
        except ValueError:
            print(" Это не число! Попробуй еще разок!")
            continue
    operator = input('Выберете действие +, -, *, /(или "стоп" для завершения)')
    if operator.lower() == "стоп" or operator.lower() == "stop":
        print('Hasta la vista...')
    elif operator not in oper:
        print("Данное действие не поддерживается. Давай начнем заново!")
        continue
    arg2 = input('Введите второй аргумент (или "стоп" для завершения): ')
    if arg2.lower() == "стоп" or arg2.lower() == "stop":
        print('Hasta la vista...')
        break
    else:
        try:
            arg2 = float(arg2)
        except ValueError:
            print(" Это не число! Попробуй еще разок!")
            continue
    if operator == "+":
        result = arg1 + arg2
    elif operator == "-":
        result = arg1 - arg2
    elif operator == "*":
        result = arg1 * arg2
    else:
        try:
            result = arg1 / arg2
        except ZeroDivisionError:
            print ("На ноль делить нельзя, двоечник! Подумай над своим поведением и начни заново!")
            continue
    count_cycle += 1
    if num:
        print(
            f'Результат: {num2words(result, lang="ru")}\nКоличество успешных решений: {num2words(count_cycle, lang="ru")}')
    else:
        print(
            f'Результат: {result}\nКоличество успешных решений: {count_cycle}')

