class Math:
    def __init__(self, first, second):
        self.first = first
        self.second = second

    def addition(self):
        return print(f'Result: {self.first + self.second}\n')

    def subtraction(self):
        return print(f'Result: {self.first - self.second}\n')

    def multiplication(self):
        return print(f'Result: {self.first * self.second}\n')

    def division(self):
        try:
            return print(f'Result: {self.first / self.second}\n')
        except ZeroDivisionError:
            print('Zero division error! Try again.\n')
