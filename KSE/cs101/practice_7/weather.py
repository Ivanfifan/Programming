import requests
key = "e90fab7014064d2c88795d9fd95afa6f"
city = input('City>>>')
link = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={key}"
data = eval(requests.get(link).text)
direction16 = ['N', 'NNE', 'NE', 'ENE', 'E', 'ESE', 'SE', 'SSE', 'S', 'SSW', 'SW', 'WSW', 'W', 'WNW', 'NW', 'NNW']
direction8 = ['N', 'NE', 'E', 'SE', 'S', 'SW', 'W', 'NW']
direction4 = ['N', 'E', 'S', 'W']

#print(int(data['wind']['deg']))
#print(direction[round(int(data['wind']['deg']) / 22.5) % 16])

def temperature(a):
    if a == 'C':
        print(round(data['main']['temp'] - 273.15))
    elif a == 'F':
        print(data['main']['temp'] - 273.15 * 1.8)
    return 'Write C or F'
temperature('C')
def wind(a):
    if a == 3:
        print(direction16[round(int(data['wind']['deg']) / 22.5) % 16])
    elif a == 2:
        print(direction8[round(int(data['wind']['deg']) / 45) % 8])
    elif a == 1:
        print(direction4[round(int(data['wind']['deg']) / 90) % 4])

wind(3)