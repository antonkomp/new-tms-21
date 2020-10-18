def my_decorator(func):
    def reverse_args(*args):
        return func(*args[::-1])

    return reverse_args


@my_decorator
def my_func(*args):
    print(*args)


my_func('first', 'second', 'third', 'fourth')
