import argparse
from datetime import datetime
import time


def create_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-n', '--name', required=True)
    parser.add_argument('-sn', '--surname', required=True)
    parser.add_argument('-tf', '--timefocus', type=int, default=25)
    parser.add_argument('-tb', '--timebreak', type=int, default=5)
    parser.add_argument('-nc', '--numbercycles', type=int, default=4)
    parser.add_argument('-tn', '--taskname', required=True)
    args_func = parser.parse_args()
    return args_func


def add_record(name, surname, taskname):
    with open('Pomodoro_log.txt', 'a') as txt_file:
        time = datetime.now().strftime("%d.%m.%Y-%H:%M:%S")
        txt_file.write(','.join([name, surname, time, taskname]))
        txt_file.write('\n')


def pomodoro(timefocus, timebreak, numbercycles):
    for i in range(numbercycles):
        total_time_focus = timefocus * 60
        print(f'Now {i + 1} cycle')
        while total_time_focus > 0:
            time.sleep(1)
            minutes = total_time_focus // 60
            if minutes // 10 < 1:
                minutes = '0' + str(minutes)
            seconds = total_time_focus % 60
            if seconds // 10 < 1:
                seconds = '0' + str(seconds)
            print(f'focus time - {minutes}:{seconds}')
            total_time_focus -= 1
        total_time_break = timebreak * 60
        while total_time_break > 0:
            time.sleep(1)
            minutes = total_time_break // 60
            if minutes // 10 < 1:
                minutes = '0' + str(minutes)
            seconds = total_time_break % 60
            if seconds // 10 < 1:
                seconds = '0' + str(seconds)
            print(f'break - {minutes}:{seconds}')
            total_time_break -= 1


if __name__ == '__main__':
    args = create_args()
    add_record(args.name, args.surname, args.taskname)
    pomodoro(args.timefocus, args.timebreak, args.numbercycles)
