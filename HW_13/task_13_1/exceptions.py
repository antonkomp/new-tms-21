def input_first_number():
    while True:
        try:
            first = float(input('First number: '))
        except ValueError:
            print('Value error! Enter the number again!')
            continue
        return first


def input_operation():
    global operation
    while True:
        operation = input('Operation: ')
        if operation not in ['+', '-', '*', '/', '0']:
            print('Value error! Enter the operation again!')
            continue
        return operation


def input_second_number():
    while True:
        try:
            second = float(input('Second number: '))
            if second == 0 and operation == '/':
                print('Zero division error! Try again.')
                continue
        except ValueError:
            print('Value error! Enter the number again!')
            continue
        return second


operation = ''
