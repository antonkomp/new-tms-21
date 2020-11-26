from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import sqlalchemy
from ui_funcs import choose_id, choose_category

e = create_engine('sqlite:///homework_orm.db')
Base = declarative_base()
Session = sessionmaker(bind=e)


class Products(Base):
    __tablename__ = 'products'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    price = Column(Integer)
    number = Column(Integer)
    comment = Column(String)

    def __init__(self, name='', price=0, number=0, comment=''):
        self.name = name
        self.price = price
        self.number = number
        self.comment = comment


def create_table():
    Base.metadata.create_all(e)


def all_products():
    session = Session()
    products = session.query(Products).all()
    session.close()
    return products


def add_product():
    name, price, number, comment = input('name: '), int(input('price: ')), int(input('number: ')), input('comment: ')
    product = Products(name=name, price=price, number=number, comment=comment)
    session = Session()
    session.add(product)
    session.commit()
    print('This product was added')


def update_product():
    products = all_products()
    ident = choose_id(products)
    category = choose_category()
    session = Session()
    session.query(Products).filter(Products.id == int(ident)).update({category: input(f'{category}: ')})
    session.commit()
    print(f'Product with id {ident} was updated')


def delete_product():
    try:
        session = Session()
        products = all_products()
        ident = choose_id(products)
        del_record = session.query(Products).filter(Products.id == ident).one()
        session.delete(del_record)
        session.commit()
        print(f'Product with id {ident} was deleted')
    except sqlalchemy.orm.exc.NoResultFound:
        print('This product does not exist')


def print_products():
    result = all_products()
    print('\nid'.rjust(2), 'name'.center(10), 'price'.center(5), 'number'.center(6), 'comment'.center(9), sep='|')
    print('------------------------------------')
    for i in result:
        print(str(i.id).rjust(2), i.name.center(10), str(i.price).center(5), str(i.number).center(6),
              i.comment.center(9), sep='|')
