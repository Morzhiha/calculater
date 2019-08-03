from calc.calculator import Calculator
from menu.menuBaseCalc import MenuBaseCalc


class ComplexCalc(MenuBaseCalc):

    def __init__(self):
        super().__init__()
        self.calculator = Calculator()

        self.methodsList = {'+': self.calculator.sum, '-': self.calculator.sub,
                         '*': self.calculator.multi, '/': self.calculator.div}

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
        a, operator, b = numbers
        print('{} {} {} = {}'.format(a, operator, b, self.getResult(a, operator, b)))

    def isComplexNumber(self, num1, num2):
        while not str(num1).isdigit() and str(num2).isdigit():
            num1, num2 = input('Некорректный формат данных! Введите ещё раз действительную и мнимую части ').split()
        return complex(int(num1), int(num2))

    def getResult(self, a, operator, b):
        return self.methodsList[operator](a, b)


    # def isOperator(self, operator):
    #     while operator not in self.methodsList.keys():
    #         operator = input('Неизвестная операция! Введите ещё раз одно из действий: +, -, *, /: ')