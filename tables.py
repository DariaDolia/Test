import sqlite3


def create_connection(db_name):
    with sqlite3.connect(db_name) as connection:
        return connection


def create_table(connection_object, table_description):
    cursor = connection_object.cursor()
    cursor.execute(table_description)


def check_if_table_exists(connection_obj, table_name):
    cursor = connection_obj.cursor()
    cursor.execute("""SELECT count(name) FROM sqlite_master WHERE type='table' AND name=?""", [table_name])
    if cursor.fetchone()[0] == 1:
        return True
    return False


def data_for_countries_table(connection_obj):
    data = [
        ('UA', 'Ukraine'),
        ('PL', 'Poland'),
        ('UK', 'United Kingdom'),
    ]

    cursor = connection_obj.cursor()
    cursor.executemany(""" insert into countries values (?, ?)""", data)
    connection_obj.commit()


def column_names(cursor, **kwargs):
    col_names = [cn[0] for cn in cursor.description]

    print(''.join([col_names[num].center(kwargs[width]) + '|' for num, width in enumerate(kwargs)]))
    print(''.join(["-" * kwargs[width] + '-' for width in kwargs]))


def width_of_columns(cursor, full_data):
    width_of_longest_data = []
    for i in range(len(full_data[0])):
        width_of_longest_data.append(max(len(str(data[i])) for data in full_data))

    width_of_col_names = [len(cn[0]) for cn in cursor.description]

    col_width = []
    for k, m in zip(width_of_longest_data, width_of_col_names):
        if k > m:
            col_width.append(k + 3)
        else:
            col_width.append(m + 3)

    return col_width



