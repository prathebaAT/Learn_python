import requests

def get_weather(city, api_key):
    base_url = "https://api.weatherbit.io/v2.0/current"
    params = {
        'city': city,
        'key': api_key,
        'units': 'M'  
    }
    response = requests.get(base_url, params=params)
    return response.json()

def parse_weather_data(data):
    if "error" in data:
        print(f"Error: {data['error']}")
        return None

    weather = {
        "temperature": data["data"][0]["temp"],
        "description": data["data"][0]["weather"]["description"],
        "humidity": data["data"][0]["rh"],
        "pressure": data["data"][0]["pres"],
        "wind_speed": data["data"][0]["wind_spd"]
    }
    return weather

api_key = "" #USE YOUR API KEY HERE
city = "kumbakonam"
weather_data = get_weather(city, api_key)

weather_info = parse_weather_data(weather_data)
if weather_info:
    print(f"Temperature: {weather_info['temperature']}°C")
    print(f"Description: {weather_info['description']}")
    print(f"Humidity: {weather_info['humidity']}%")
    print(f"Pressure: {weather_info['pressure']} hPa")
    print(f"Wind Speed: {weather_info['wind_speed']} m/s")
