import requests

class OpenWeatherMap:
    def __init__(self, city):
        self.api_key = '2ffda98bfbe8f5d17280fa7d817d1e2b'
        self.city = city
        self.data = None
        try:
            url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={self.api_key}"
            response = requests.get(url)
            self.data = response.json()
        except requests.exceptions.RequestException as e:
            print(f"Помилка при отриманні даних: {e}")
            self.data = None

    def get_temp(self, unit='Kelvin'):
        try:
            temp_kelvin = self.data['main']['temp']

            if unit == 'Celsius':
                return round(temp_kelvin - 273.15, 1)
            elif unit == 'Fahrenheit':
                return round((temp_kelvin - 273.15) * 9 / 5 + 32, 1)
            else:  # Kelvin
                return temp_kelvin

        except KeyError:
            return "Помилка"

    def get_weather(self):
        try:
            return self.data['weather'][0]['main']
        except (KeyError, IndexError):
            return 'Помилка'

    def get_city(self):
        if not self.data:
            return "Дані відсутні"
        else:
            return self.data['name']

    def get_text(self):
        if not self.data:
            return "Дані відсутні"
        else:
            text = "Дані з API:\n"
            for key, value in self.data.items():
                text += f"{key}: {value}\n"
            return text

    def get_wind(self):
        if not self.data:
            return "Дані відсутні"
        else:
            try:
                deg = self.data['wind']['deg']
                storona = ['Північ','Схід','Південь','Захід']

                return storona[round(int(deg // 90) % 4)]

            except KeyError:
                return "Помилка"
    def show(self):
        if not self.data: return "Помилка"
        return f'Сьогодні в {self.get_city()} погода буде - {self.get_weather()}. Температура за вікном - {self.get_temp("Celsius")}. Вітер: {self.get_wind()}'


def ai(data:dict) -> str:
    if not data:
        return "Дані відсутні"

    temp = data['main']['temp'] - 273.15
    status = data['weather'][0]['main']
    advice = ""

    if temp < 10:
        advice += "Холодно, не забудьте шапку!"
    else:
        advice += "Тепло, можна без шапки"

    if status == 'Rain':
        advice += " Йде дощ, беріть парасольку"
    else:
        advice += " Дощу немає"

    return advice


if __name__ == "__main__":
    city = input("Введіть місто: ")
    weather = OpenWeatherMap(city)
    info = weather.show()
    print(info)
    recommendation = ai(weather.data)
    print("Порада:", recommendation)
    filename = "6_Семенченко.txt"
    with open(filename, "a", encoding="utf-8") as f:
        f.write(f"{info} | {recommendation}\n")