import sqlite3

DB_PATH = 'data_store/piano.db'

sql_insert_into_table ='''
    INSERT INTO piano(name, price, year_of_production)
    VALUES (?, ?, ?)
'''

while True:
    piano_name = input('Upisite naziv piana: ')
    piano_price = float(input('unesite cijenu: '))
    piano_yop = int(input('Unesite godinu proizvodnje: '))

    try:
        with sqlite3.connect(DB_PATH) as conn:
            cursor = conn.cursor()
            cursor.execute(sql_insert_into_table, (piano_name, piano_price, piano_yop))


    except Exception as ex:
        print(f'Dogodila se greska {ex}')
    
    next_piano = input('Zelite li unjeti novi piano (da/ne): ')
    if next_piano.lower() != 'da':
        break


