import requests
import json

# Your OpenWeatherMap API Key
API_KEY = 'afed0c37366050569e22198d0a082ea7'

def get_weather(city_name):
    base_url = 'http://api.openweathermap.org/data/2.5/weather'
    params = {'q': city_name, 'appid': API_KEY, 'units': 'metric'}  # You can change units to 'imperial' for Fahrenheit

    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        data = response.json()
        return data
    else:
        return None

def main():
    print("Welcome to the Weather App!")
    city_name = input("Enter the name of a city: ")

    weather_data = get_weather(city_name)

    if weather_data:
        # Extract relevant information from the JSON response
        temperature = weather_data['main']['temp']
        description = weather_data['weather'][0]['description']
        humidity = weather_data['main']['humidity']

        print(f"Weather in {city_name}:")
        print(f"Temperature: {temperature}°C")
        print(f"Description: {description}")
        print(f"Humidity: {humidity}%")
    else:
        print("City not found or an error occurred.")

# if __name__ == '__main__':
#     main()
main()
