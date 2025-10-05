import requests
key = "e90fab7014064d2c88795d9fd95afa6f"
city = input('City>>>')
link = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={key}"
data = eval(requests.get(link).text)
direction = ['N','NNE','NE','ENE','E','ESE','SE','SSE','S','SSW','SW','WSW','W','WNW','NW','NNW']
print(int(data['wind']['deg']))
print(direction[round(int(data['wind']['deg']) / 22.5) % 16])