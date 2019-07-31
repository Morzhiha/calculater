import calculate


def init():
    a = int(input('Первое число '))
    b = int(input('Второе число '))
    d = input('Введите одно из действий: +, -, *, /: ')

    print('{} {} {} = {}'.format(a, d, b, calculate.calc(a, b, d)))
    again()


def again():
    ans = input('Хотите снова? Нажмите Д(да) или Н(нет)')
    if ans.upper() == 'Д':
        init()
    else:
        print('Спасибо за внимание')