from calc.calculate import Calculator

calculator = Calculator()


class MenuBaseCalc:

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
        while not self.isNumber(a):
            a = int(input('Некорректный формат данных! Введите ещё раз первое число '))
        d = input('Введите одно из действий: +, -, *, /: ')
        while d not in ('+' , '-', '*', '/'):
            d = input('Неизвестная операция! Введите ещё раз одно из действий: +, -, *, /: ')
        b = input('Второе число ')
        while not self.isNumber(b):
            b = int(input('Некорректный формат данных! Введите ещё раз второе число '))
        if d == '/':
            while b == 0:
                b = int(input('Делить на ноль нельзя! Введите ещё раз второе число '))
        return int(a), d, int(b)

    def getResult(self, a, d, b):
        operatorList = {'+': calculator.sum(a, b), '-': calculator.sub(a, b),
                        '*': calculator.multi(a, b), '/': calculator.div(a, b)}
        if d in operatorList.keys():
            return operatorList[d]
        else:
            print('Неизвестная операция')

    def answer(self, s):
        a, d, b = s
        print('{} {} {} = {}'.format(a, d, b, self.getResult(a, d, b)))

    def isNumber(self, a):
        return str(a).isdigit()
