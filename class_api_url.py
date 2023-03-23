import requests


class BaseApi:

    @staticmethod
    def get_response(url, headers=None, params=None):
        response = requests.get(url, headers=headers, params=params)
        rj = response.json()
        return rj


class IpAddressApi(BaseApi):

    url = 'https://api.ipify.org?format=json'

    def __str__(self):
        return f'Your IP-address is: {self.get_response(self.url)["ip"]}'


class CityCoordinatesApi(BaseApi):

    url = 'https://api.api-ninjas.com/v1/city'
    headers = {'X-Api-Key': 'cXI98FHH1z5uWErFnlFiTPLpqIbMIPN1QuhElaUN'}

    def get_city_info(self):
        your_city = input('Enter a city: ').title()
        params = {'name': {your_city}}
        res_json = self.get_response(self.url, headers=self.headers, params=params)
        if res_json:
            return self.get_city_coordinates(res_json)
        elif not res_json:
            return 'There in no such city'
        else:
            return 'error'

    @staticmethod
    def get_city_coordinates(response):
        city_name = response[0]['name']
        latitude = response[0]['latitude']
        longitude = response[0]['longitude']
        return city_name, latitude, longitude


class CurrentWeatherApi(CityCoordinatesApi):

    def get_current_weather(self):
        city_info = self.get_city_info()

        if isinstance(city_info, str):
            print(city_info)

        elif isinstance(city_info, tuple):
            city_name, latitude, longitude = city_info
            url = 'https://api.open-meteo.com/v1/forecast'
            params = {'latitude': latitude, 'longitude': longitude, 'current_weather': True}

            weather_json = self.get_response(url, params=params)

            current_temp = weather_json['current_weather']["temperature"]
            print(f'The current temperature in {city_name} is {current_temp}')
