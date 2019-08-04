from calc.calculator import Calculator
from menu.menuBaseCalc import MenuBaseCalc


class ComplexNumber:
    def __init__(self, re, im):
        self.re = re
        self.im = im

    def getRe(self):
        return self.re

    def getIm(self):
        return self.im


class MethodsComplexCalc:

    def __init__(self):
        self.calculator = Calculator()

    def sum(self, z1, z2):
        return ComplexNumber(z1.getRe() + z2.getRe(), z1.getIm() + z2.getIm())

    def sub(self, z1, z2):
        return ComplexNumber(z1.getRe() - z2.getRe(), z1.getIm() - z2.getIm())

    def multi(self, z1, z2):
        return ComplexNumber(z1.getRe()*z2.getRe() - z1.getIm()*z2.getIm(),
                             z1.getRe()*z2.getIm() + z1.getIm()*z2.getRe())

    def div(self, z1, z2):
        d = z2.getRe()*z2.getRe() + z2.getIm()*z2.getIm()
        return ComplexNumber((z1.getRe()*z2.getRe() + z1.getIm()*z2.getIm())/d,
                             (z1.getIm()*z2.getRe() - z1.getRe()*z2.getIm())/d)


class ComplexCalc(MenuBaseCalc):

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
        a, b = input('Введите действительную и мнимую части первого числа ').split()
        z1 = self.isComplexNumber(a, b)

        operator = input('Введите одно из действий: +, -, *, /: ')
        self.isOperator(operator)
        a, b = input('Введите действительную и мнимую части второго числа ').split()
        z2 = self.isComplexNumber(a, b)
        if operator == '/':
            z2 = self.divisionByZero(b)
        return z1, operator, z2

    def answer(self, numbers):
        z1, operator, z2 = numbers
        print('({}+{}i) {} ({}+{}i) = {}'.format(z1.getRe(), z1.getIm(), operator, z2.getRe(), z2.getIm(),
                                     self.getResult(z1, operator, z2)))

    def isComplexNumber(self, num1, num2):
        while not str(num1).isdigit() and str(num2).isdigit():
            num1, num2 = input('Некорректный формат данных! Введите ещё раз действительную и мнимую части ').split()
        return ComplexNumber(int(num1), int(num2))

    def getResult(self, a, operator, b):
        z = self.methodsComplList[operator](a, b)
        return '(' + str(z.getRe()) + '+' + str(z.getIm()) + 'i)'


