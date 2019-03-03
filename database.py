import sqlite3 as sq

conn = sq.connect('ray1.db')
c = conn.cursor()

def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS stuff(unix REAL,date TEXT,key TEXT,value REAL)')
def insert():
    c.execute("INSERT INTO stuff VALUES('1414','01/01/2001','PY','5')")
    conn.commit()
    c.close()
    conn.close()

create_table()
insert()
