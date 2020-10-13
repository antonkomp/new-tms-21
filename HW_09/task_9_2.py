print((lambda **kwargs: {key * 2: value for key, value in kwargs.items()})(abc=5, python=1, ahah=3))
