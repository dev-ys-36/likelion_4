import requests
import json

city = 'Seoul'
key = '9d7f20530b1230f538e365cf476ef85b'
lang = 'kr'
#units='metric'
#units='imperial'

url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={key}&lang={lang}&units=metric'

result = requests.get(url)
#print(result.text)

data = json.loads(result.text)

print(data['name'],'의 날씨입니다.')
print('날씨는', data['weather'][0]['description'],'입니다.')
print('현재 온도는', data['main']['temp'],'입니다.')
print('체감', data['main']['feels_like'],'일 거에요.')
print('최저 기온은', data['main']['temp_min'],'입니다.')
print('최고 기온은', data['main']['temp_max'],'입니다.')
print('습도는', data['main']['humidity'],'입니다.')
print('기압은', data['main']['pressure'],'입니다.')
print('풍향은',  data['wind']['deg'],'입니다.')
print('풍속은',  data['wind']['speed'],'입니다.')