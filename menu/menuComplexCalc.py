from calc.calculator import Calculator
from calc.complexCalc import ComplexCalc
from structure.complexNumber import ComplexNumber
from menu.menuBaseCalc import MenuBaseCalc


class MenuComplexCalc(MenuBaseCalc):

    def __init__(self):
        super().__init__()
        self.calculator = Calculator()

        self.complexCalc = ComplexCalc()
        self.methodsComplList = {'+': self.complexCalc.sum, '-': self.complexCalc.sub,
                         '*': self.complexCalc.multi, '/': self.complexCalc.div}

    def mainMenu(self):
        flag = True
        while flag:
            self.answer(self.getComplex())
            f = input('Хотите снова? Нажмите Д(да) или Н(нет)')
            if f.upper() != 'Д' and f.upper() != 'ДА':
                flag = False
                print('Спасибо за внимание')

    def getComplex(self):
        a = input('Введите действительную часть первого числа ')
        a = super().isNumber(a)
        b = input('Введите мнимую часть первого числа ')
        b = super().isNumber(b)
        z1 = ComplexNumber(a, b)

        operator = input('Введите одно из действий: +, -, *, /: ')
        super().isOperator(operator)
        a = input('Введите действительную часть второго числа ')
        a = super().isNumber(a)
        b = input('Введите мнимую часть второго числа ')
        b = super().isNumber(b)

        if operator == '/':
            a = self.isNumber(self.divisionByZero(a))
            b = self.isNumber(self.divisionByZero(b))
        z2 = ComplexNumber(a, b)
        return z1, operator, z2

    def answer(self, numbers):
        z1, operator, z2 = numbers
        print('{} {} {} = {}'.format(z1, operator, z2, self.getResult(z1, operator, z2)))

    def getResult(self, a, operator, b):
        return self.methodsComplList[operator](a, b)
