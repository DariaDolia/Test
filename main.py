import class_api_url
from options_menu import options


def main():
    while True:
        chosen_option = options()
        if chosen_option == 1:
            ip_address_url = class_api_url.IpAddressApi()
            print(ip_address_url)

        elif chosen_option == 2:
            weather_in_the_city = class_api_url.CurrentWeatherApi()
            weather_in_the_city.get_current_weather()

        elif chosen_option == 3:
            return
        else:
            print('Your choice out of scope\n')


if __name__ == '__main__':
    main()
