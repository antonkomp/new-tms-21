from classes import Point, Circle, Triangle, Square, Figure


def main():
    list_figure = [
        Circle(Point(1, 1), 5),
        Circle(Point(3, 6), 8),
        Circle(Point(), 4),
        Triangle(Point(1, 1), Point(3, 4), Point(5, 1)),
        Triangle(Point(2, 3), Point(5, 7), Point(10, 2)),
        Triangle(Point(-5, 1), Point(11, 3), Point(4, 6)),
        Square(Point(2, 1), Point(1, 6)),
        Square(Point(7, -5), Point(2, 8)),
        Square(Point(5, 4), Point(8, 2))
    ]

    for i, item in enumerate(list_figure):
        print(f'Figure area {i} - {item.area()} m²')


if __name__ == '__main__':
    main()
