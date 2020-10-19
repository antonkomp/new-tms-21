from random import randint
from datetime import datetime
from time import time

date = []
for i in range(30):
    timestamp = randint(1, int(time()))
    data = datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d\n')
    date.append(data)

filename = 'date_file.txt'
with open(filename, 'w') as data:
    data.writelines(date)

min_date = '3'
with open(filename, 'r') as file_read:
    for line in file_read.readlines():
        if min_date > line:
            min_date = line
print(min_date)
