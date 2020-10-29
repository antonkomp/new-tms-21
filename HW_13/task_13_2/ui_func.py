from classes import Math
import exceptions


def calculator():
    while True:
        print('Please enter numbers and operation (to exit enter in operation \'0\'):')
        first = exceptions.input_first_number()
        operation = exceptions.input_operation()
        if operation == '0':
            break
        second = exceptions.input_second_number()
        ans = Math(first, second)
        if operation == '+':
            ans.addition()
        elif operation == '-':
            ans.subtraction()
        elif operation == '*':
            ans.multiplication()
        elif operation == '/':
            ans.division()
