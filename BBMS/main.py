# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


import sqlite3
"Bootcamp2023.db"
conn = sqlite3.connect("Bootcamp2023.db")



conn.execute("delete from donors where d_no=1")
conn.commit()


