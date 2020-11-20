from classes import Math
import exceptions


def calculator():
    def input_first_number():
        while True:
            try:
                fir = float(input('First number: '))
            except ValueError:
                print('Value error! Enter the number again!')
                continue
            return fir

    def input_operation():
        while True:
            try:
                oper = input('Operation: ')
                if oper not in ['+', '-', '*', '/', '0']:
                    raise exceptions.OperationValueError
            except exceptions.OperationValueError:
                print('Value error! Enter the operation again!')
                continue
            return oper

    def input_second_number():
        while True:
            try:
                sec = float(input('Second number: '))
                if sec == 0 and operation == '/':
                    raise exceptions.OperationZeroDivisionError
            except ValueError:
                print('Value error! Enter the number again!')
                continue
            except exceptions.OperationZeroDivisionError:
                print('Zero division error! Try again.')
                continue
            return sec

    print('Please enter numbers and operation (to exit enter in operation \'0\'):')
    first = input_first_number()
    operation = input_operation()
    if operation == '0':
        return
    second = input_second_number()
    ans = Math(first, second)
    if operation == '+':
        return ans.addition()
    elif operation == '-':
        return ans.subtraction()
    elif operation == '*':
        return ans.multiplication()
    elif operation == '/':
        return ans.division()
