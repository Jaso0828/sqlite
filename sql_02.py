import sqlite3

DB_PATH = 'data_stor/piano.db'

sql_create_table = ('''
    CREATE TABLE IF NOT EXISTS piano
    (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        price REAL,
        year_of_production INTEGER NULL
   );
''')

try:
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute(sql_create_table)

    conn.commit()

except Exception as ex:
    print(f'Dogodila se greska {ex}')

finally:
    if conn:
        conn.close()
        print('Konekcija na bazi je zatvorena')
   
