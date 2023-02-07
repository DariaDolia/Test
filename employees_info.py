import sqlite3

WIDTH_OF_NAME_COL = 15
WIDTH_OF_CODE_COL = 6
WIDTH_OF_SALARY_COL = 12
FULL_WIDTH = WIDTH_OF_NAME_COL + WIDTH_OF_CODE_COL + WIDTH_OF_SALARY_COL + 3


def create_new_db():
    with sqlite3.connect('employees.db') as db:
        cursor = db.cursor()
    cursor.execute("""create table if not exists employees_info(
        name text not null,
        country_code text,
        salary integer);
        """)


def show_all_employees():
    with sqlite3.connect('employees.db') as db:
        cursor = db.cursor()
    cursor.execute('select * from employees_info')
    for name, country_code, salary in cursor.fetchall():
        print(name.ljust(WIDTH_OF_NAME_COL, ' '), country_code.center(WIDTH_OF_CODE_COL, ' '),
              f"{salary:{WIDTH_OF_SALARY_COL},.2f}", '', sep='|')


def create_new_employees(name, country_code, salary):
    with sqlite3.connect('employees.db') as db:
        cursor = db.cursor()
        cursor.execute('insert into employees_info values (?, ?, ?)', [name, country_code, salary])
        db.commit()


def delete_employee(name_of_employee):
    list_of_names = []
    with sqlite3.connect('employees.db') as db:
        cursor = db.cursor()
        cursor.execute('select name from employees_info')
        for i in cursor.fetchall():
            list_of_names.append(i[0])
        if name_of_employee in list_of_names:
            cursor.execute('delete from employees_info where name=?', [name_of_employee])
        else:
            print('There is not such name in the table')


def main():

    print('1. Show all employees')
    print('2. Create a new employees')
    print('3. Delete an employees')
    print('4. Exit')

    create_new_db()

    while True:
        option = int(input('\nChoose an option from list above: '))
        if option == 1:
            print()
            print('name'.center(WIDTH_OF_NAME_COL, ' '), 'code'.center(WIDTH_OF_CODE_COL, ' '),
                  'salary ($)'.center(WIDTH_OF_SALARY_COL, ' '), '', sep='|')
            print('-' * FULL_WIDTH)
            show_all_employees()

        elif option == 2:
            name = input('enter a name: ').title()
            while True:
                country_code = input('enter a country code UA, PL, UK: ').upper()
                if country_code in ['UA', 'PL', 'UK']:
                    salary = float(input('enter a salary: '))
                    create_new_employees(name, country_code, salary)
                    break
                else:
                    print('\nYou enter incorrect country code. Try again')

        elif option == 3:
            name_of_employee = input('\nEnter a NAME of employee you wanna delete: ').title()
            delete_employee(name_of_employee)

        elif option == 4:
            return


main()
