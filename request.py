import requests


api_key = 'a452bbabff8901ab43ae07426f8a3823'


url = f'http://api.openweathermap.org/data/2.5/weather?q=London&APPID={api_key}'


get_requests = requests.get(url)


print (get_requests.json()['wind'])

