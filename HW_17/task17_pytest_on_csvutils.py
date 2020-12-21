import pytest
import csv_utils


@pytest.fixture()
def csv_f():
    return 'my_csv_file.csv'


@pytest.fixture()
def field():
    return 'First name, Last name, Age'


@pytest.fixture()
def rows():
    return 'Anton, Baranau, 34', 'Vladimir, Shedko, 19'


class TestCsv:
    def test_read_csv(self, csv_f):
        actual = csv_utils.read_csv(csv_f)
        expected = (['First name', 'Last name', 'Age'], [['Anton', 'Baranau', '34'], ['Vladimir', 'Shedko', '19']])
        assert actual == expected

    def test_prepare_csv_data(self, field, rows):
        actual = csv_utils.prepare_csv_data(field, rows)
        expected = (
            ['First name', ' Last name', ' Age'], [['Anton', ' Baranau', ' 34'], ['Vladimir', ' Shedko', ' 19']])
        assert actual == expected

    def test_print_csv(self, csv_f):
        def expected_print():
            field = ['First name', ' Last name', ' Age']
            rows = [['Anton', ' Baranau', ' 34'], ['Vladimir', ' Shedko', ' 19']]
            for col in field:
                print(col.ljust(30, " "), end='')
            print()
            for row in rows:
                for col in row:
                    print(col.ljust(30, " "), end='')
                print()

        assert csv_utils.print_csv(csv_f) == expected_print()


if __name__ == '__main__':
    TestCsv()
