from random import randint
from datetime import datetime
from time import time
import csv

date = []
for i in range(30):
    timestamp = randint(1, int(time()))
    data = datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d')
    date.append(data)

filename = 'date_file.csv'
with open(filename, 'w', newline='') as csvdata:
    csvwriter = csv.writer(csvdata)
    csvwriter.writerow(date)

with open(filename, 'r', newline='') as file_read:
    csvreader = csv.reader(file_read)
    list_csv_file = next(csvreader)

min_date = list_csv_file[0]
for i in range(len(list_csv_file) - 1):
    if min_date > list_csv_file[i + 1]:
        min_date = list_csv_file[i + 1]
print(min_date)
