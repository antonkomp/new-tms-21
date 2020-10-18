import csv, requests
from time import time
from datetime import datetime

DAYS = 6  # data are taken for 6 days, not 7, because you cannot get data for more than 6 days from the site for free
api_url = 'https://api.openweathermap.org/data/2.5/onecall/timemachine'
params = {
    'lat': '53.842761',  # width of the Minsk
    'lon': '27.702095',  # longitude of the Minsk
    'dt': int(time() - 1),  # current time
    'units': 'metric',  # units of measure
    'appid': '466673d528f019d751e7973b7a9d1bb1'  # API key
}
fields = ['date', 'location', 'temperature', 'wind speed']
rows_data = [[] for i in range(DAYS)]
sum_temp = 0
sum_wind_speed = 0

for i in range(DAYS):
    res = requests.get(api_url, params=params)
    data = res.json()
    rows_data[i].append(datetime.fromtimestamp(params['dt']).strftime('%Y-%m-%d %H:%M:%S'))
    rows_data[i].append('Minsk')
    rows_data[i].append(data['current']['temp'])
    sum_temp += data['current']['temp']
    rows_data[i].append(data['current']['wind_speed'])
    sum_wind_speed += data['current']['wind_speed']
    # the parameter must be changed after executing the cycle, since its initial value is already set
    params['dt'] -= 86400

rows_average_data = [
    ['average temperature', round(sum_temp / DAYS, 2)],
    ['average wind speed', round(sum_wind_speed / DAYS, 2)]
]

filename = 'weather_in_Minsk.csv'
with open(filename, 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(fields)
    csvwriter.writerows(rows_data)
    csvwriter.writerows(rows_average_data)
