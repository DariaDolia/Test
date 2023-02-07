import sqlite3


def create_new_db():
    with sqlite3.connect('employees.db') as db:
        cursor = db.cursor()
    cursor.execute("""create table if not exists employees_info(
        name text not null,
        country_code check (country_code in ('UA', 'PL', 'UK')),
        salary integer);
        """)


def show_all_employees():
    with sqlite3.connect('employees.db') as db:
        cursor = db.cursor()
    cursor.execute('select * from employees_info')
    for name, country_code, salary in cursor.fetchall():
        print(name.ljust(15, ' '), country_code.center(6, ' '), f"{salary:12,.2f}", '', sep='|')


def create_new_employees(name, country_code, salary):
    with sqlite3.connect('employees.db') as db:
        cursor = db.cursor()
    while True:
        try:
            cursor.execute('insert into employees_info values (?, ?, ?)', [name, country_code, salary])
            db.commit()
            return
        except sqlite3.IntegrityError:
            print('\nYou enter incorrect country code. Try again')
            country_code = input('enter a country code : ').upper()


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
            print('name'.center(15, ' '), 'code'.center(6, ' '), 'salary ($)'.center(12, ' '), '', sep='|')
            print('-' * 36)
            show_all_employees()

        elif option == 2:
            name = input('enter a name: ').title()
            country_code = input('enter a country code UA, PL, UK: ').upper()
            salary = float(input('enter a salary: '))
            create_new_employees(name, country_code, salary)

        elif option == 3:
            name_of_employee = input('\nEnter a NAME of employee you wanna delete: ').title()
            delete_employee(name_of_employee)

        elif option == 4:
            return


main()