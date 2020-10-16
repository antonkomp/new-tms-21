import csv, requests
from time import time
from datetime import datetime

api_url = 'https://api.openweathermap.org/data/2.5/onecall/timemachine'
params = {
    'lat': '53.842761',  # width of the Minsk
    'lon': '27.702095',  # longitude of the Minsk
    'dt': int(time() - 1),  # current time
    'units': 'metric',  # units of measure
    'appid': '466673d528f019d751e7973b7a9d1bb1'  # API key
}
fields = ['date', 'location', 'temperature', 'wind speed']
rows_data = [[0 for x in range(4)] for j in range(6)]
sum_temp = 0
sum_wind_speed = 0
# данные берутся за 6 дней, а не за 7, т.к. с сайта бесплатно нельзя получить данные более чем за 6 дней
for i in range(6):
    res = requests.get(api_url, params=params)
    data = res.json()
    rows_data[i][0] = datetime.fromtimestamp(params['dt']).strftime('%Y-%m-%d %H:%M:%S')
    rows_data[i][1] = 'Minsk'
    rows_data[i][2] = data['current']['temp']
    sum_temp += data['current']['temp']
    rows_data[i][3] = data['current']['wind_speed']
    sum_wind_speed += data['current']['wind_speed']
    params['dt'] -= 86400

rows_average_data = [
    ['average temperature', round(sum_temp / 6, 2)],
    ['average wind speed', round(sum_wind_speed / 6, 2)]
]

filename = 'weather_in_Minsk.csv'
with open(filename, 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(fields)
    csvwriter.writerows(rows_data)
    csvwriter.writerows(rows_average_data)
