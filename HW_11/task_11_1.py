class Vehicle:
    def __init__(self, type, speed, color):
        self.__type = type
        self.__speed = speed
        self.__color = color

    def drive(self):
        print('Drive')

    def brake(self):
        print('Brake')

    def get_type(self):
        return self.__type

    def set_type(self, type):
        self.__type = type

    def get_speed(self):
        return self.__speed

    def set_speed(self, speed):
        self.__speed = speed

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, color):
        self.__color = color


class Man:
    def __init__(self, gender, name, age, nationality):
        self.gender = gender
        self.__name = name
        self.__age = age
        self.__nationality = nationality

    def speek(self):
        print('Long live Belarus!')

    def be_silent(self):
        print('%%%')

    def get_gender(self):
        return self.gender

    def set_gender(self, gender):
        self.gender = gender

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_age(self):
        return self.__age

    def set_age(self, age):
        self.__age = age

    @property
    def nationality(self):
        return self.__nationality

    @nationality.setter
    def nationality(self, nationality):
        self.__nationality = nationality


class Phone:
    def __init__(self, company, year, price):
        self.__company = company
        self.__year = year
        self.__price = price

    def call(self):
        print('The phone rings')

    def write_message(self):
        print("To write a message")

    def get_company(self):
        return self.__company

    def set_company(self, company):
        self.__company = company

    def get_year(self):
        return self.__year

    def set_year(self, year):
        self.__year = year

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price):
        self.__price = price


class House:
    def __init__(self, type_of_building, year, number_of_storeys):
        self.__type_of_building = type_of_building
        self.__year = year
        self.__number_of_storeys = number_of_storeys

    def sale(self):
        print('House for sale')

    def empty(self):
        print('Empty house')

    def get_type_of_building(self):
        return self.__type_of_building

    def set_type_of_building(self, type_of_building):
        self.__type_of_building = type_of_building

    def get_year(self):
        return self.__year

    def set_year(self, year):
        self.__year = year

    @property
    def number_of_storeys(self):
        return self.__number_of_storeys

    @number_of_storeys.setter
    def number_of_storeys(self, number_of_storeys):
        self.__number_of_storeys = number_of_storeys


class Football_Club:
    def __init__(self, country, name, titles, rating):
        self.__country = country
        self.__name = name
        self.__titles = titles
        self.__rating = rating

    def buy_player(self):
        print('The club buys a good player')

    def sale_player(self):
        print('The club sells an unwanted player')

    def get_country(self):
        return self.__country

    def set_country(self, country):
        self.__country = country

    def get_titles(self):
        return self.__titles

    def set_titles(self, titles):
        self.__titles = titles

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    @property
    def rating(self):
        return self.__rating

    @rating.setter
    def rating(self, rating):
        self.__rating = rating
