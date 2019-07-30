
def calc():
    a = int(input('Первое число '))
    b = int(input('Второе число '))
    d = input('Введите одно из действий: +, -, *, /: ')

    print('{} {} {} = {}'.format(a, d, b, i(a, b, d)))
    again()
    

def i(a, b, d):
    if d == '+':
        return a + b
    elif d == '-':
        return a - b
    elif d == '*':
        return a * b
    elif d == '/':
        try:
            return a / b
        except ZeroDivisionError:
            return 'Делить на ноль нельзя'
    else:
        print('Неизвестная операция')


def again():
    ans = input('Хотите снова? Нажмите Д(да) или Н(нет)')
    if ans.upper() == 'Д':
        calc()
    else:
        print('Спасибо за внимание')

calc()
