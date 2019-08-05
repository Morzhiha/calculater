from calc.calculator import Calculator
from structure.complexNumber import ComplexNumber


class ComplexCalc(Calculator):

    def __init__(self):
        super().__init__()


    def sum(self, z1, z2):
        return ComplexNumber(super().sum(z1.getRe(), z2.getRe()), super().sum(z1.getIm(), z2.getIm()))

    def sub(self, z1, z2):
        return ComplexNumber(super().sub(z1.getRe(), z2.getRe()), super().sub(z1.getIm(), z2.getIm()))

    def multi(self, z1, z2):
        return ComplexNumber(super().sub(super().multi(z1.getRe(), z2.getRe()), super().multi(z1.getIm(), z2.getIm())),
                             super().sum(super().multi(z1.getRe(), z2.getIm()), super().multi(z1.getIm(), z2.getRe())))

    def div(self, z1, z2):
        print(z2.getRe())
        a = super().sum(super().multi(z1.getRe(), z2.getRe()), super().multi(z1.getIm(), z2.getIm()))
        b = super().sub(super().multi(z1.getIm(), z2.getRe()), super().multi(z1.getRe(), z2.getIm()))
        d = super().sum(super().multi(z2.getRe(), z2.getRe()), super().multi(z2.getIm(), z2.getIm()))
        return ComplexNumber(super().div(a, d), super().div(b, d))





