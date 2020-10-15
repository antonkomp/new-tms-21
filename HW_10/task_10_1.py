import csv
from random import randint

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
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(fields)
    csvwriter.writerows(rows)

filename2 = 'report_file.txt'
age_groups = ['Age groups:', '1-12', '13-18', '19-25', '26-40', '40+']
number = ['Number:', 0, 0, 0, 0, 0]
for i in range(10):
    if 1 <= rows[i][2] <= 12:
        number[1] += 1
    elif 13 <= rows[i][2] <= 18:
        number[2] += 1
    elif 19 <= rows[i][2] <= 25:
        number[3] += 1
    elif 26 <= rows[i][2] <= 40:
        number[4] += 1
    elif 40 <= rows[i][2] < 50:
        number[5] += 1

with open(filename2, 'w') as report:
    for i in range(6):
        report.write('%10s' % age_groups[i])
        report.write('%10s \n' % number[i])
