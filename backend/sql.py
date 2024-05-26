

import sqlite3

con = sqlite3.connect("backend\db.sqlite3")
cursor = con.cursor()
sql_command = """
           DELETE FROM webserver_food WHERE Name = 'meat'

            """
cursor.execute(sql_command)

con.commit()

con.close()

