import requests,json

def get_weather(city_name, api_key):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city_name,
        "appid": api_key,
        "units": "metric"  #imperial -2- Fahrenheit

    }

    try:
        response = requests.get(base_url, params=params)
        data = response.json()

        if response.status_code == 200:
            weather_info = {
                "city": data["name"],
                "temperature": data["main"]["temp"]
            }
            return weather_info
        else:
            print(f"Error: {data['message']}")
            return None

    except requests.exceptions.RequestException as i:
        print(f"An error occurred: {i}")
        return None 

if __name__== "__main__":
    api_key =  "85e4d2e4c00095dd832fbe25874e9eff" #My api

    while True:
        city_name = input("Enter your city name: ")


        weather_info = get_weather(city_name, api_key)

        if weather_info:
            print(f"The temperature in {city_name}: {weather_info['temperature']}°C")
            
        else:
            print("Please enter a valid city name.")
