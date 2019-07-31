from calc.calculate import Calculator

calculator = Calculator()


def init():
    a = int(input('Первое число '))
    b = int(input('Второе число '))
    d = input('Введите одно из действий: +, -, *, /: ')

    print('{} {} {} = {}'.format(a, d, b, calculator.calc(a, b, d)))
    again()


def again():
    ans = input('Хотите снова? Нажмите Д(да) или Н(нет)')
    if ans.upper() == 'Д' or ans.upper() == 'Да':
        init()
    else:
        print('Спасибо за внимание')
