import argparse
from datetime import datetime
from time import monotonic


def create_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-n', '--name', required=True)
    parser.add_argument('-sn', '--surname', required=True)
    parser.add_argument('-hr', '--hours', type=int, required=True)
    parser.add_argument('-m', '--minutes', type=int, required=True)
    parser.add_argument('-s', '--seconds', type=int, required=True)
    args_func = parser.parse_args()
    return args_func


def add_record(name, surname):
    with open('records.txt', 'a') as txt_file:
        time = datetime.now().strftime("%d.%m.%Y-%H:%M:%S")
        txt_file.write(','.join([name, surname, time]))
        txt_file.write('\n')


def timer(hours, minutes, seconds):
    total_seconds = hours * 3600 + minutes * 60 + seconds
    monotonic_number = monotonic()
    while True:
        if total_seconds == 0:
            print('ALARM!!!')
            break
        if monotonic() - monotonic_number > 1:
            monotonic_number = monotonic()
            hours = total_seconds // 3600
            if hours // 10 < 1:
                hours = '0' + str(hours)
            minutes = total_seconds % 3600 // 60
            if minutes // 10 < 1:
                minutes = '0' + str(minutes)
            seconds = total_seconds % 60
            if seconds // 10 < 1:
                seconds = '0' + str(seconds)
            total_seconds -= 1
            print(f'{hours}:{minutes}:{seconds}')


if __name__ == '__main__':
    args = create_args()
    add_record(args.name, args.surname)
    timer(args.hours, args.minutes, args.seconds)
