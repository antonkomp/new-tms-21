from flask import Flask
import datetime

app = Flask(__name__)

@app.route('/home_page')
def home_page():
    return str(datetime.date.today())


if __name__ == '__main__':
    app.run()
