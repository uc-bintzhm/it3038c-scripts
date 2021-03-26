import json
import requests


print('Please enter your zip code:')
zip = input()

r = requests.get('http://api.openweathermap.org/data/2.5/weather?zip=%s&appid=1b884b3cd0d8c393e9e7f3e6d9d61258' % zip)

data=r.json()
print(data['weather'][0]['description'])