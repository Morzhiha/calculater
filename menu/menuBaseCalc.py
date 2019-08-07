from calc.calculator import Calculator


class MenuBaseCalc:

    def __init__(self):
        self.calculator = Calculator()

        self.methodsList = {'+': self.calculator.sum, '-': self.calculator.sub,
                         '*': self.calculator.multi, '/': self.calculator.div}

    def getResult(self, a, operator, b):
        return self.methodsList[operator](a, b)

    def answer(self, numbers):
        a, operator, b = numbers
        print('{} {} {} = {}'.format(a, operator, b, self.getResult(a, operator, b)))

    def isNumber(self, num):
        while not str(num).isdigit():
            num = input('Некорректный формат данных! Введите ещё раз число ')
        return int(num)

    def isOperator(self, operator):
        while operator not in self.methodsList.keys():
            operator = input('Неизвестная операция! Введите ещё раз одно из действий: +, -, *, /: ')

    def divisionByZero(self, b):
        while b == 0:
            b = input('Делить на ноль нельзя! Введите ещё раз второе число ')
        return b

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
            b = self.divisionByZero(b)
        return a, operator, b