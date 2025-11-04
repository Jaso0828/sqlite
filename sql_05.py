import sqlite3

DB_PATH = 'data_store/piano.db'

sql_insert_into_table ='''
    SELECT * FROM piano
'''

sql_select_one = '''
    SELECT * FROM piano
    WHERE id IS (?)
'''

try:
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute(sql_select_one, (1,))
        results = cursor.fetchall()
        print(results)

except Exception as ex:
    print(f'Dogodila se greska {ex}')




