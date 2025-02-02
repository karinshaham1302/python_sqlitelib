import sqlite3
import os


db_name: str = "18_12_2024db.db"
conn = sqlite3.connect(db_name)
conn.row_factory = sqlite3.Row
cursor = conn.cursor()



cursor.execute("DROP TABLE IF EXISTS shopping")



cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        age INTEGER NOT NULL
    )
''')
print("Table created or already exists.")



cursor.execute('''
    INSERT INTO users (name, age)
    VALUES (?, ?)
''', ("Alice", 30))
cursor.execute('''
    INSERT INTO users (name, age)
    VALUES (?, ?)
''', ("Bob", 25))
print("Data inserted.")


conn.commit()


cursor.execute("SELECT * FROM sales")
rows = cursor.fetchall()


result_list = [list(row) for row in rows]
result_dict = [dict(row) for row in rows]
result_tuple = [tuple(row) for row in rows]

for result in [result_list, result_dict, result_tuple]:
    print(result)


cursor.execute("SELECT * FROM shopping")
print('Select - All items:')
result1 = [tuple(row) for row in cursor.fetchall()]
print(result1)
print()




cursor.execute("update sales set product_name=? where id =?",
               ('Wireless Mouse 3.0', 1))

conn.commit()


cursor.execute("UPDATE shopping SET name = ? WHERE name LIKE ?",
               ('Bisli', 'Bamba'))
conn.commit()



cursor.execute("DELETE FROM shopping WHERE name LIKE 'Orange'")
conn.commit()





if os.path.exists(db_name):
    os.remove(db_name)
    print(f"Database file '{db_name}' was deleted.")
else:
    print(f"Database file '{db_name}' does not exist.")




conn.close()
