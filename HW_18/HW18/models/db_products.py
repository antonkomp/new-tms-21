from sqlalchemy_utils import database_exists, create_database
from config import db, app


class Product(db.Model):
    id = db.Column('product_id', db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    price = db.Column(db.Float)
    amount = db.Column(db.Integer)
    comment = db.Column(db.String(100))

    def __init__(self, name, price, amount, comment):
        self.name = name
        self.price = price
        self.amount = amount
        self.comment = comment

if not database_exists(db.engine.url):
   create_database(db.engine.url)
db.init_app(app)
db.create_all()
