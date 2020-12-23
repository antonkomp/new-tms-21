from sqlalchemy import create_engine, ForeignKey
from sqlalchemy import Column, Integer, Float, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from ui_funcs import choose_brand_category, choose_car_category

DB_USER = 'postgres'
DB_PASSWORD = 'postgres'
DB_NAME = 'homework_16'
eng = create_engine(f'postgresql://{DB_USER}:{DB_PASSWORD}@localhost/{DB_NAME}')
Base = declarative_base()
Session = sessionmaker(bind=eng)
session = Session()


class Brand(Base):
    __tablename__ = 'brand'
    id = Column(Integer, primary_key=True)
    name = Column(String)


class Car(Base):
    __tablename__ = 'car'
    id = Column(Integer, primary_key=True)
    model = Column(String)
    release_year = Column(Integer)
    brand_id = Column(Integer, ForeignKey('brand.id'), nullable=False)
    brand = relationship('Brand', foreign_keys='Car.brand_id', lazy='joined', backref='brand')


def create_table():
    Base.metadata.create_all(eng)


def add_brand():
    name = input('name: ')
    brand = Brand(name=name)
    session.add(brand)
    session.commit()


def get_brand(id_brand):
    brand = session.query(Brand).filter_by(id=id_brand).first()
    return brand


def update_brand():
    id_brand = input('id brand: ')
    category = choose_brand_category()
    session.query(Brand).filter(Brand.id == int(id_brand)).update({category: input('\nNew value: ')})
    session.commit()
    print(f'Brand with id {id_brand} was updated')


def delete_brand():
    id_brand = input('Delete id brand: ')
    brand = get_brand(id_brand)
    session.delete(brand)
    session.commit()
    print(f'Brand with id {id_brand} was deleted')


def print_brands():
    result = session.query(Brand).all()
    print('id', 'name'.center(10), sep='|')
    print('-----------------------------')
    for i in result:
        print(str(i.id).ljust(2), i.name.center(10), sep='|')


def add_car():
    model, release_year, id_brand = input('model: '), int(input('release year: ')), int(input('id brand: '))
    brand = get_brand(id_brand)
    car = Car(model=model, release_year=release_year, brand=brand)
    session.add(car)
    session.commit()


def update_car():
    id_car = input('id car: ')
    car = session.query(Car).filter_by(id=id_car).first()
    category = choose_car_category()
    if category == 'brand':
        print_brands()
        id_brand = input('id брэнда: ')
        brand = get_brand(id_brand)
        car.brand = brand
        session.add(car)
    else:
        session.query(Car).filter(Car.id == int(id_car)).update({category: input('\nNew value: ')})
    session.commit()
    print(f'Car with id {id_car} was updated')


def delete_car():
    id_car = input('Delete id car: ')
    car = session.query(Car).filter(Car.id == id_car).one()
    session.delete(car)
    session.commit()
    print(f'Car with id {id_car} was deleted')


def print_cars():
    result = session.query(Car).all()
    print('\nid', 'name'.center(10), 'release year', 'brand'.center(10), sep='|')
    print('------------------------------------')
    for i in result:
        print(str(i.id).ljust(2), i.model.center(10), str(i.release_year).center(12),
              str(i.brand.name).center(10), sep='|')
