import sqlite3

db_location = "data.db"

connection = sqlite3.connect(db_location)
cursor = connection.cursor()

create_table = "CREATE TABLE IF NOT EXISTS student (name text, fees real, clg text)"
cursor.execute(create_table)

# delete_table = "DROP TABLE IF EXISTS items"
# cursor.execute(delete_table)
connection.commit()
connection.close()