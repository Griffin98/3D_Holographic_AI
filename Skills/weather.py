import requests

API_ADDRESS = 'https://api.openweathermap.org/data/2.5/weather?units=metric&appid=dcc49fd08d599f33f5ed3decb159c93a&q='

def get_weather(location):
    url = API_ADDRESS + location
    json_data = requests.get(url).json()
    print(json_data)
    weather = {
        'location': location,
        'temperature': json_data['main']['temp'],
        'description': json_data['weather'][0]['description'],
        'icon': json_data['weather'][0]['icon'],
        'humidity': json_data['main']['humidity'],
        'pressure': json_data['main']['pressure'],
        'wind_speed': json_data['wind']['speed']
    }
    return weather

if __name__ == "__main__":
    city = input("Enter Location:")
    get_weather(city)
