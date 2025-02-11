import sqlite3

conn = sqlite3.connect(":memory:")
cursor = conn.cursor()
cursor.execute("""
create table people (id integer primary key, name text, count integer)
""")
cursor.execute("""insert into people (name, count) values ('Bob', 15)""")
