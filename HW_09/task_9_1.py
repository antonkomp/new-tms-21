list_strings = ['Python works on different platforms (Windows, Mac, Linux, Raspberry Pi, etc).',
                'Python has a simple syntax similar to the English language.',
                'Python has syntax that allows developers to write programs with fewer lines than some other programming languages.',
                'Python runs on an interpreter system, meaning that code can be executed as soon as it is written. This means that prototyping can be very quick.',
                'Python can be treated in a procedural way, an object-oriented way or a functional way.']

format_list_strings = [f'{i} - {string}' for i, string in enumerate(list_strings)]
for i in format_list_strings:
    print(i)
