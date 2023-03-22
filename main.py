import functions
from options_menu import options


def main():
    while True:
        chosen_option = options()

        if chosen_option == 1:
            functions.get_ip_address()

        elif chosen_option == 2:
            data = functions.get_city()
            if data:
                city, latitude, longitude = functions.get_city_coordinates(data)
                functions.get_weather(city, latitude, longitude)
            elif not data:
                print('There is no such city.')

        elif chosen_option == 3:
            return
        else:
            print('Your choice out of scope\n')


if __name__ == '__main__':
    main()
