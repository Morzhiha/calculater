
class ComplexNumber:
    def __init__(self, re, im):
        self.re = re
        self.im = im

    def getRe(self):
        return self.re

    def getIm(self):
        return self.im

    def __str__(self):
        z = '(' + str(self.getRe()) + str(self.getIm()) + 'i' + ')' if self.getIm() < 0 else '(' + str(self.getRe()) + ')' \
            if self.getIm() == 0 else '(' + str(self.getRe()) + '+' + str(self.getIm()) + 'i' + ')'
        return z
