from funcs import *


def main():
    create_table()
    while True:
        print('\nChoose your number:\n  1. Add brand\n  2. Update brand\n  3. Delete brand\n'
              '  4. Print brands\n  5. Add car\n  6. Update car\n  7. Delete car\n  8. Print cars')
        num = int(input('Your number: '))
        if num == 0:
            break
        elif num == 1:
            add_brand()
        elif num == 2:
            update_brand()
        elif num == 3:
            delete_brand()
        elif num == 4:
            print_brands()
        elif num == 5:
            add_car()
        elif num == 6:
            update_car()
        elif num == 7:
            delete_car()
        elif num == 8:
            print_cars()


if __name__ == '__main__':
    main()
