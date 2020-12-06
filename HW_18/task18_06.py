from flask import Flask, redirect, url_for

app = Flask(__name__)


@app.route('/my_word/<word>')
def user(word):
    if len(word) % 2 == 0:
        new_word = ''
        for i in range(len(word)):
            if i % 2 == 0:
                new_word += word[i]
        return new_word
    else:
        return word


if __name__ == '__main__':
    app.run(debug=True)
