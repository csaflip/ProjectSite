import sqlite3

connection = sqlite3.connect('database.db')


with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO budget (category, notes, dollar) VALUES (?, ?, ?)",
            ('Bread', 'Bread from the store', 5)
            )
cur.execute("INSERT INTO budget (category, notes, dollar) VALUES (?, ?, ?)",
            ('Grocs', '', 55)
            )
cur.execute("INSERT INTO budget (category, notes, dollar) VALUES (?, ?, ?)",
            ('Rent', '', 780)
            )

connection.commit()
connection.close()