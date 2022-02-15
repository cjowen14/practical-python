from msvcrt import getwch
import requests

def get_weather():
    api_key = "844754848552cb95aad0b02829522060"
    lat = "41.22276"
    long = "-111.97042"
    url = "http://api.openweathermap.org/data/2.5/weather?lat=" + lat + "&lon=" + long + "&appid=" + api_key + "&units=imperial"

    request = requests.get(url)
    json = request.json()

    description = json.get("weather")[0].get("description")
    temp_min = json.get("main").get("temp_min")
    temp_max = json.get("main").get("temp_max")

    return{'description': description,
            'temp_min': temp_min,
            'temp_max': temp_max}

def main():
    weather_dict = get_weather()

    # Print the results
    print("Today's forecast is", weather_dict.get('description'))
    print("The minimum temperature is", weather_dict.get('temp_min'))
    print("The maximum temperature is", weather_dict.get('temp_max'))

main()