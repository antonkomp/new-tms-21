def choose_category():
    print('\nChoose category to update:\n  1. name\n  2. price\n  3. number\n  4. comment')
    num = int(input('Your number: '))
    if num == 1:
        return 'name'
    elif num == 2:
        return 'price'
    elif num == 3:
        return 'number'
    elif num == 4:
        return 'comment'


def choose_id(products):
    print('\nSelect product id:')
    for product in products:
        print(product.id, end=' ')
    chosen_id = input('\nYour choice: ')
    return chosen_id
