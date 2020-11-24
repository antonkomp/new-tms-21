import ui_func


def main():
    while True:
        result = ui_func.calculator()
        if result is None:
            break
        else:
            print(f'Result: {result}\n')


if __name__ == '__main__':
    main()
