from calc.calculator import Calculator
from calc.complexCalc import MethodsComplexCalc
from calc.complexNumber import ComplexNumber
from menu.menuBaseCalc import MenuBaseCalc


class MenuComplexCalc(MenuBaseCalc):

    def __init__(self):
        super().__init__()
        self.calculator = Calculator()

        self.methodsComplex = MethodsComplexCalc()
        self.methodsComplList = {'+': self.methodsComplex.sum, '-': self.methodsComplex.sub,
                         '*': self.methodsComplex.multi, '/': self.methodsComplex.div}

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
        a = self.isNumber(a)
        b = input('Введите мнимую часть первого числа ')
        b = self.isNumber(b)
        z1 = self.isComplexNumber(a, b)

        operator = input('Введите одно из действий: +, -, *, /: ')
        self.isOperator(operator)
        a = input('Введите действительную часть второго числа ')
        b = input('Введите мнимую часть второго числа ')
        z2 = self.isComplexNumber(a, b)
        if operator == '/':
            z2 = self.divisionByZero(b)
        return z1, operator, z2

    def answer(self, numbers):
        z1, operator, z2 = numbers
        print('{} {} {} = {}'.format(z1, operator, z2, self.getResult(z1, operator, z2)))

    def isComplexNumber(self, num1, num2):
        while not str(num1).isdigit() and str(num2).isdigit():
            num1, num2 = input('Некорректный формат данных! Введите ещё раз действительную и мнимую части ').split()
        return ComplexNumber(int(num1), int(num2))

    def getResult(self, a, operator, b):
        z = self.methodsComplList[operator](a, b)
        return z
