def my_decorator(func):
    def odd_numbers(list_num):
        for i in list_num:
            if i % 2 == 0:
                list_num.remove(i)
        return func(list_num)

    return odd_numbers


@my_decorator
def all_numbers(list_num):
    print(list_num)


all_numbers([i * 3 for i in range(1, 20)])
