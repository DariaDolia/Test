
import tables
import options


WIDTH_NAME_COL = 15
WIDTH_COUNTRY_COL = 18
WIDTH_SALARY_COL = 15
FULL_WIDTH = WIDTH_NAME_COL + WIDTH_COUNTRY_COL + WIDTH_SALARY_COL + 3


create_employees_info = """create table employees_info(
    name text not null,
    country_code text,
    salary integer not null);"""

create_countries = """create table countries (
        code text not null,
        country text not null);"""


def main():
    connection = tables.create_connection('employees.db')

    if tables.check_if_table_exists(connection, 'employees_info') is False:
        tables.create_table(connection, create_employees_info)

    if tables.check_if_table_exists(connection, 'countries') is False:
        tables.create_table(connection, create_countries)
        tables.data_for_countries_table(connection)

    while True:
        options.options()
        try:
            option = int(input('\nChoose an option from list above: '))
        except ValueError:
            print('You entered invalid value. Try again')
            continue

        if option == 1:
            options.show_all_employees(connection, WIDTH_NAME_COL, WIDTH_COUNTRY_COL, WIDTH_SALARY_COL, FULL_WIDTH)

        elif option == 2:
            name = input('enter a name: ').title().rstrip()
            while True:
                country_code = input('enter a country code UA, PL, UK: ').upper().strip()
                if country_code in ['UA', 'PL', 'UK', '']:
                    salary = float(input('enter a salary: ').replace(',', '.'))
                    options.create_new_employees(connection, name, country_code, salary)
                    break
                else:
                    print('\nYou enter incorrect country code. Try again')

        elif option == 3:
            name_of_employee = input('\nEnter a NAME of employee you wanna delete: ').title()
            options.delete_employee(connection, name_of_employee)

        elif option == 4:
            options.country_statistics(connection, WIDTH_COUNTRY_COL)

        elif option == 5:
            return


main()
