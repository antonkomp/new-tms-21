def is_palindrome(word):
    rev = word[::-1]
    if word == rev:
        print(f'{word} - palindrome')


first_word = 'python'
is_palindrome(first_word)
second_word = 'level'
is_palindrome(second_word)
third_word = 'noon'
is_palindrome(third_word)
