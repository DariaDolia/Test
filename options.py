import tables


def options():
    print()
    print('1. Show all employees')
    print('2. Create a new employees')
    print('3. Delete an employees')
    print('4. Country statistics')
    print('5. Exit')


def show_all_employees(connection_obj):
    table_for_employees_info = """select 
            e.name, coalesce(c.country, 'Unknown') country, e.salary 'salary ($)' 
            from employees_info e left join countries c
            on e.country_code = c.code"""

    cursor = connection_obj.cursor()
    cursor.execute(table_for_employees_info)
    data = cursor.fetchall()
    tables.table_output(cursor, data)


def create_new_employees(connection_obj, name, country_code, salary):
    cursor = connection_obj.cursor()
    cursor.execute("""insert into employees_info values (?, ?, ?)""", [name, country_code, salary])
    connection_obj.commit()


def delete_employee(connection_obj, name_of_employee):
    cursor = connection_obj.cursor()
    cursor.execute('delete from employees_info where name=?', [name_of_employee])
    if cursor.rowcount:
        connection_obj.commit()
        return
    print('There is not such name in the table')


def country_statistics(connection_obj):
    table_for_statistics = """select 
            coalesce(c.country, 'Unknown') country, count(*) num_employees, 
            sum(salary) 'total salary ($)', max(salary) 'max salary ($)'
            from employees_info e left join countries c 
            on e.country_code = c.code
            group by country;"""

    cursor = connection_obj.cursor()
    cursor.execute(table_for_statistics)
    data = cursor.fetchall()
    tables.table_output(cursor, data)
