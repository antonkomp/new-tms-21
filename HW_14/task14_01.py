import argparse
from datetime import datetime
from time import sleep


def create_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-n', '--name', required=True)
    parser.add_argument('-l', '--lastname', required=True)
    parser.add_argument('-o', '--hours', type=int, required=True)
    parser.add_argument('-m', '--minutes', type=int, required=True)
    parser.add_argument('-s', '--seconds', type=int, required=True)
    args_func = parser.parse_args()
    return args_func


def add_record(name, lastname):
    with open('records.txt', 'a') as txt_file:
        time = datetime.now().strftime("%d.%m.%Y-%H:%M:%S")
        txt_file.write(','.join([name, lastname, time]))
        txt_file.write('\n')


def timer(hours, minutes, seconds):
    total_seconds = hours * 3600 + minutes * 60 + seconds
    while total_seconds:
        hours = total_seconds // 3600
        minutes = total_seconds % 3600 // 60
        seconds = total_seconds % 60
        total_seconds -= 1
        print(f'{hours:02}:{minutes:02}:{seconds:02}')
        sleep(1)
    print('ALARM!!!')


if __name__ == '__main__':
    args = create_args()
    add_record(args.name, args.lastname)
    timer(args.hours, args.minutes, args.seconds)
