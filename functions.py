import class_api_url


def get_ip_address():
    ip_url = class_api_url.ApiUrl('https://api.ipify.org')
    print(f'Your IP-address is: {ip_url.get_response().text}')


def get_city():
    city = input('Enter a city: ')
    city_url = class_api_url.ApiUrl('https://api.api-ninjas.com/v1/city',
                                    headers={'X-Api-Key': 'cXI98FHH1z5uWErFnlFiTPLpqIbMIPN1QuhElaUN'},
                                    params={'name': {city}})

    response = city_url.get_response()
    if not response.json():
        return None
    elif response.json():
        return response


def get_city_coordinates(response):
    name = response.json()[0]['name']
    latitude = response.json()[0]['latitude']
    longitude = response.json()[0]['longitude']
    return name, latitude, longitude


def get_weather(city, lat, long):
    weather_url = class_api_url.ApiUrl('https://api.open-meteo.com/v1/forecast',
                                       params={'latitude': lat, 'longitude': long, 'current_weather': True})

    response = weather_url.get_response()

    current_temp = response.json()['current_weather']["temperature"]
    print(f'The current temperature in {city} is {current_temp}')