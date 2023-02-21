import sqlite3


employees_info = """create table employees_info(
    name text not null,
    country_code text,
    salary real not null);"""

countries = """create table countries (
        code text not null,
        country text not null);"""

data_for_countries = [
        ('UA', 'Ukraine'),
        ('PL', 'Poland'),
        ('UK', 'United Kingdom'),
    ]

table_descriptions = [employees_info, countries]


def create_connection(db_name):
    with sqlite3.connect(db_name) as connection:
        return connection


def create_table(connection_object, table_names, descriptions):
    for table, description in zip(table_names, descriptions):
        if check_if_table_exists(connection_object, table) is False:
            cursor = connection_object.cursor()
            cursor.execute(description)
            if table == 'countries':
                cursor.executemany(""" insert into countries values (?, ?)""", data_for_countries)
                connection_object.commit()


def check_if_table_exists(connection_obj, table_name):
    cursor = connection_obj.cursor()
    cursor.execute("""SELECT count(name) FROM sqlite_master WHERE type='table' AND name=?""", [table_name])
    if cursor.fetchone()[0] == 1:
        return True
    return False


def width_of_columns(cursor, full_data):
    col_names = [cn[0] for cn in cursor.description]

    max_width = []
    for i in range(len(full_data[0])):
        data_width = max([len(str(data[i])) for data in full_data])
        max_width.append(max(data_width, len(col_names[i])) + 3)

    print(''.join([col_names[num].center(width) + '|' for num, width in enumerate(max_width)]))
    print(''.join(["-" * width + '-' for width in max_width]))

    return max_width
