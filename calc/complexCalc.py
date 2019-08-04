from calc.calculator import Calculator
from calc.complexNumber import ComplexNumber


class MethodsComplexCalc:

    def __init__(self):
        self.calculator = Calculator()

    def sum(self, z1, z2):
        return ComplexNumber(self.calculator.sum(z1.getRe(),z2.getRe()), self.calculator.sum(z1.getIm(), z2.getIm()))

    def sub(self, z1, z2):
        return ComplexNumber(self.calculator.sub(z1.getRe(), z2.getRe()), self.calculator.sub(z1.getIm(), z2.getIm()))

    def multi(self, z1, z2):
        return ComplexNumber(self.calculator.sub(self.calculator.multi(z1.getRe(), z2.getRe()), self.calculator.multi(z1.getIm(), z2.getIm())),
                             self.calculator.sum(self.calculator.multi(z1.getRe(), z2.getIm()), self.calculator.multi(z1.getIm(), z2.getRe())))

    def div(self, z1, z2):
        a = self.calculator.sum(self.calculator.multi(z1.getRe(), z2.getRe()), self.calculator.multi(z1.getIm(), z2.getIm()))
        print(a)
        b = self.calculator.sub(self.calculator.multi(z1.getIm(), z2.getRe()), self.calculator.multi(z1.getRe(), z2.getIm()))
        d = self.calculator.sum(self.calculator.multi(z2.getRe(), z2.getRe()), self.calculator.multi(z2.getIm(), z2.getIm()))
        return ComplexNumber(self.calculator.div(a, d),   self.calculator.div(b, d))





