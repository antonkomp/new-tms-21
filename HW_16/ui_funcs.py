def choose_brand_category():
    print('\nChoose category to update:\n  1. name')
    num = int(input('Your number: '))
    if num == 1:
        return 'name'


def choose_car_category():
    print('\nChoose category to update:\n  1. model\n  2. release_year\n  3. brand')
    num = int(input('Your number: '))
    if num == 1:
        return 'model'
    elif num == 2:
        return 'release_year'
    elif num == 3:
        return 'brand'
