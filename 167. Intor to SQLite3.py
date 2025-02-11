import sqlite3

conn = sqlite3.connect("datafile.db")
cursor = conn.cursor()
# cursor.execute("""
# create table people (id integer primary key, name text, count integer)
# """)
# cursor.execute("""insert into people (name, count) values ('Bob', 15)""")

# result = cursor.execute(
#     "select * from people where name=:username", {"username": "Bob"})
# print(result.fetchmany(2))

cursor.execute("""update people set count = :usercount where name = :username""", {
               "username": 'Bob', "usercount": 39})
result = cursor.execute("select * from people")
print(result.fetchall())

conn.commit()
conn.close()
