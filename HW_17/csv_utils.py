import csv


def read_csv(filename):
    rows = []
    with open(filename, 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        fields = next(csvreader)
        for row in csvreader:
            rows.append(row)
    return fields, rows


def prepare_csv_data(fileds, rows):
    list_fields = fileds.split(',')
    list_rows = []
    for row in rows:
        list_rows.append(row.split(','))
    return list_fields, list_rows


def print_csv(filename):
    fields, rows = read_csv(filename)
    for col in fields:
        print(col.ljust(30, " "), end='')
    print()
    for row in rows:
        for col in row:
            print(col.ljust(30, " "), end='')
        print()
