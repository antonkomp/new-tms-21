import csv
from random import randint
from collections import OrderedDict

filename = 'my_csv_file.csv'
fields = ['First name', 'Last name', 'Age']
rows = [
    ['Anton', 'Baranau', randint(1, 50)],
    ['Vladimir', 'Shedko', randint(1, 50)],
    ['Dzmitry', 'Ushal', randint(1, 50)],
    ['Max', 'Sinitskiy', randint(1, 50)],
    ['Artyom', 'Semenau', randint(1, 50)],
    ['Sonia', 'Tishkova', randint(1, 50)],
    ['Alina', 'Sharets', randint(1, 50)],
    ['Andrey', 'Kazarovets', randint(1, 50)],
    ['Alexandr', 'Boldysh', randint(1, 50)],
    ['Svetlana', 'Kuchmareva', randint(1, 50)],
]
with open(filename, 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile, quoting=csv.QUOTE_NONNUMERIC)
    csvwriter.writerow(fields)
    csvwriter.writerows(rows)

rows_read = []
with open(filename, 'r', newline='') as csvread:
    csvreader = csv.reader(csvread, quoting=csv.QUOTE_NONNUMERIC)
    fields = next(csvreader)
    for row in csvreader:
        rows_read.append(row)

od = OrderedDict()
od['Age groups:'] = 'Number:'
od['1-12'] = 0
od['13-18'] = 0
od['19-25'] = 0
od['26-40'] = 0
od['40+'] = 0

for i in range(len(rows_read)):
    if 1 <= rows_read[i][2] <= 12:
        od['1-12'] += 1
    elif 13 <= rows_read[i][2] <= 18:
        od['13-18'] += 1
    elif 19 <= rows_read[i][2] <= 25:
        od['19-25'] += 1
    elif 26 <= rows_read[i][2] <= 40:
        od['26-40'] += 1
    elif 40 <= rows_read[i][2] < 50:
        od['40+'] += 1

filename2 = 'report_file.txt'
with open(filename2, 'w') as report:
    for key, value in od.items():
        report.write('%10s' % key)
        report.write('%10s \n' % value)
