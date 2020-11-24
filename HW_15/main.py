from funcs import create_table, add_product, update_product, delete_product, print_products


def main():
    create_table()
    while True:
        print('\nChoose your number:\n  1. Add product\n  2. Update product\n  3. Delete product\n  4. Print products')
        number = int(input('Your number: '))
        if number == 0:
            break
        elif number == 1:
            add_product()
        elif number == 2:
            update_product()
        elif number == 3:
            delete_product()
        elif number == 4:
            print_products()


if __name__ == '__main__':
    main()
