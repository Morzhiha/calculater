from calc.calculator import Calculator


class MenuBaseCalc:

    def __init__(self):
        self.calculator = Calculator()

        self.operatorsList = {'+': self.calculator.sum, '-': self.calculator.sub,
                         '*': self.calculator.multi, '/': self.calculator.div}

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
        self.isOperator(operator)
        b = input('Второе число ')
        b = self.isNumber(b)
        if operator == '/':
            while b == 0:
                b = input('Делить на ноль нельзя! Введите ещё раз второе число ')
        return a, operator, b

    def getResult(self, a, operator, b):
        return self.operatorsList[operator](a, b)

    def answer(self, s):
        print('{} {} {} = {}'.format(s[0], s[1], s[2], self.getResult(s[0], s[1], s[2])))

    def isNumber(self, a):

        while not str(a).isdigit():
            a = input('Некорректный формат данных! Введите ещё раз число ')

        return int(a)

    def isOperator(self, operator):
        while operator not in ('+', '-', '*', '/'):
            operator = input('Неизвестная операция! Введите ещё раз одно из действий: +, -, *, /: ')
