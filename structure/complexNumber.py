
class ComplexNumber:
    def __init__(self, re, im):
        self.re = re
        self.im = im

    def getRe(self):
        return self.re

    def getIm(self):
        return self.im

    def __str__(self):
        if self.getIm() < 0:
            return '(' + str(self.getRe()) + str(self.getIm()) + 'i' + ')'
        elif self.getIm() == 0:
            return '(' + str(self.getRe()) + ')'
        return '(' + str(self.getRe()) + '+' + str(self.getIm()) + 'i' + ')'
