import requests
from requests.exceptions import RequestException


class BaseApi:

    @staticmethod
    def method_get(url, headers=None, params=None):
        try:
            response = requests.get(url, headers=headers, params=params)
            return response.json()
        except RequestException as error:
            return error        # or this variant: return f'Error occurred'


class IpAddressApi(BaseApi):

    url = 'https://api.ipify.org?format=json'

    def get_result(self):
        ip_info = self.method_get(self.url)

        if isinstance(ip_info, RequestException):
            print(ip_info)
            return
        print(f'Your IP-address is: {ip_info["ip"]}')


class CityCoordinatesApi(BaseApi):

    url = 'https://api.api-ninjas.com/v1/city'
    headers = {'X-Api-Key': 'cXI98FHH1z5uWErFnlFiTPLpqIbMIPN1QuhElaUN'}

    def get_result(self):
        your_city = input('Enter a city: ').title()
        params = {'name': your_city}
        city_info = self.method_get(self.url, headers=self.headers, params=params)

        if isinstance(city_info, RequestException):
            return city_info
        elif not city_info:
            return 'There in no such city'
        return self.get_city_coordinates(city_info)

    @staticmethod
    def get_city_coordinates(city_info):
        city_name = city_info[0]['name']
        latitude = city_info[0]['latitude']
        longitude = city_info[0]['longitude']
        return city_name, latitude, longitude


class CurrentWeatherApi(CityCoordinatesApi):

    def get_result(self):
        city_info = super().get_result()

        if isinstance(city_info, RequestException):
            print(city_info)

        elif isinstance(city_info, str):
            print(city_info)

        elif isinstance(city_info, tuple):
            city_name, latitude, longitude = city_info
            url = 'https://api.open-meteo.com/v1/forecast'
            params = {'latitude': latitude, 'longitude': longitude, 'current_weather': True}

            weather_json = self.method_get(url, params=params)
            if isinstance(weather_json, RequestException):
                print(weather_json)
            else:
                current_temp = weather_json['current_weather']["temperature"]
                print(f'The current temperature in {city_name} is {current_temp}')



