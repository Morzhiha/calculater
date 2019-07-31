
class Calculator:

    def sum(self, a, b):
        return a + b

    def sub(self, a, b):
        return a - b

    def multi(self, a, b):
        return a * b

    def div(self, a, b):
        return a / b

    def calc(self, a, b, d):
        if d == '+':
            self.sum(a, b)
        elif d == '-':
            self.sub(a, b)
        elif d == '*':
            self.multi(a, b)
        elif d == '/':
            try:
                self.div(a, b)
            except ZeroDivisionError:
                return 'Делить на ноль нельзя'
        else:
            print('Неизвестная операция')
