from calc.calculator import Calculator


class MenuBaseCalc:

    def __init__(self):
        self.calculator = Calculator()

    def mainMenu(self):
        flag = True
        while flag:
            self.answer(self.getInputData())
            f = input('Хотите снова? Нажмите Д(да) или Н(нет)')
            if f.upper() != 'Д' and f.upper() != 'ДА':
                flag = False
                print('Спасибо за внимание')

    def getInputData(self):
        a = input('Первое число ')
        a = self.isNumber(a)
        operator = input('Введите одно из действий: +, -, *, /: ')
        while operator not in ('+', '-', '*', '/'):
            operator = input('Неизвестная операция! Введите ещё раз одно из действий: +, -, *, /: ')
        b = input('Второе число ')
        b = self.isNumber(b)
        if operator == '/':
            while b == 0:
                b = input('Делить на ноль нельзя! Введите ещё раз второе число ')
        return int(a), operator, int(b)

    def getResult(self, a, operator, b):

        operatorsList = {'+': self.calculator.sum(a, b), '-': self.calculator.sub(a, b),
                        '*': self.calculator.multi(a, b), '/': self.calculator.div(a, b)}
        print(operatorsList)
        return operatorsList[operator]

    def answer(self, s):
        a, operator, b = s
        print('{} {} {} = {}'.format(a, operator, b, self.getResult(a, operator, b)))

    def isNumber(self, a):

        while not str(a).isdigit():
            a = input('Некорректный формат данных! Введите ещё раз число ')

        return int(a)
