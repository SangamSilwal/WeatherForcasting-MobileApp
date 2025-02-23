import requests


def get_weather_data(city_name):
    data = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid=fb4dc52ed1e5429a5bff6a4076148144").json()
    if data.get("cod") == "404":
        return None
    forcast_dict = {
        "name":data["name"],
        "Weather_Status" : data["weather"][0]["description"],
        "temp" : data["main"]["temp"],
        "feels_like":data["main"]["feels_like"],
        "temp_min":data["main"]["temp_min"],
        "temp_max":data["main"]["temp_max"],
        "pressure":data["main"]["pressure"],
    }
    return forcast_dict