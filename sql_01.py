import sqlite3


conn = sqlite3.connect('data_store/piano.db')

cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS piano
    (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        price REAL,
        year_of_production INTEGER NULL
   );
''')

conn.commit()


conn.close()

