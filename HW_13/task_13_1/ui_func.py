import func
import exceptions


def calculator():
    while True:
        print('Please enter numbers and operation (to exit enter in operation \'0\'):')
        first = exceptions.input_first_number()
        operation = exceptions.input_operation()
        if operation == '0':
            break
        second = exceptions.input_second_number()
        if operation == '+':
            func.addition(first, second)
        elif operation == '-':
            func.subtraction(first, second)
        elif operation == '*':
            func.multiplication(first, second)
        elif operation == '/':
            func.division(first, second)
