
def calc(a, b, d):
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
