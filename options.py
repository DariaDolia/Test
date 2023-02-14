
def options():
    print()
    print('1. Show all employees')
    print('2. Create a new employees')
    print('3. Delete an employees')
    print('4. Exit')


def show_all_employees(connection_obj, width_name, width_country, width_salary):
    cursor = connection_obj.cursor()
    cursor.execute("""select e.name, c.country, e.salary 
        from employees_info e left join countries c
        on e.country_code = c.code""")

    for name, country, salary in cursor.fetchall():
        if country is None:
            country = ''
        print(name.ljust(width_name, ' '), country.center(width_country, ' '),
              f"{salary:{width_salary},.2f}", '', sep='|')


def create_new_employees(connection_obj, name, country_code, salary):
    cursor = connection_obj.cursor()
    cursor.execute('insert into employees_info values (?, ?, ?)', [name, country_code, salary])
    connection_obj.commit()


def delete_employee(connection_obj, name_of_employee):
    cursor = connection_obj.cursor()
    cursor.execute('select name from employees_info')
    for name in cursor:
        if name[0] == name_of_employee:
            cursor.execute('delete from employees_info where name=?', [name_of_employee])
            connection_obj.commit()
            return
    print('There is not such name in the table')
