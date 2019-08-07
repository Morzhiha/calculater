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

    def answer(self, numbers):
        z1, operator, z2 = numbers
        print('{} {} {} = {}'.format(z1, operator, z2, self.getResult(z1, operator, z2)))

    def getResult(self, a, operator, b):
        return self.methodsComplList[operator](a, b)

    def inputComplex(self):
        a = input('Введите действительную часть числа ')
        a = super().isNumber(a)
        b = input('Введите мнимую часть числа ')
        b = super().isNumber(b)
        return ComplexNumber(a, b)

    def divisionByZero(self, z):
        while z.getRe() == 0 and z.getIm() == 0:
            print('Делить на ноль нельзя!')
            z = self.inputComplex()
        return z
    def getComplex(self):
        z1 = self.inputComplex()

        operator = input('Введите одно из действий: +, -, *, /: ')
        super().isOperator(operator)

        z2 = self.inputComplex()
        if operator == '/' and z2.getIm() == 0 and z2.getRe() == 0:
            z2 = self.divisionByZero(z2)
        return z1, operator, z2

    def mainMenu(self):
        flag = True
        while flag:
            self.answer(self.getComplex())
            f = input('Хотите снова? Нажмите Д(да) или Н(нет)')
            if f.upper() != 'Д' and f.upper() != 'ДА':
                flag = False
                print('Спасибо за внимание')
