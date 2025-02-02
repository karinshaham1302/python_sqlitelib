import sqlite3

def connect_db(my_db_name):
    my_conn = sqlite3.connect(my_db_name)
    my_conn.row_factory = sqlite3.Row
    my_cursor = my_conn.cursor()
    return my_conn, my_cursor


# def execute_query(my_cursor, my_conn, query) -> None:
#     '''
#     execute a modify query (insert, update, delete)
#     # PEP8
#     :param my_cursor: sqlite cursor
#     :param my_conn:  sqlite connection
#     :param query: sql string query
#     :return: None
#     '''
#     my_cursor.execute(query)
#     my_conn.commit()


def print_color(message, color="red"):
    match color:
        case "red":
            COLOR = '\033[31m'
            RESET = '\033[0m'
        case "blue":
            COLOR = '\033[34m'
            RESET = '\033[0m'
        case _:
            COLOR = '\033[31m'
            RESET = '\033[0m'
    print(f"{COLOR}{message}{RESET}")


def read_query(my_cursor, query):
    my_cursor.execute(query)
    rows = my_cursor.fetchall()
    result_list = [list(row) for row in rows]
    result_dict = [dict(row) for row in rows]
    result_tuple = [tuple(row) for row in rows]
    return result_tuple


def update_query(my_cursor, my_conn, query, param):
    my_cursor.execute(query, param)
    my_conn.commit()
