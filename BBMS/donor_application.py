import sqlite3
"Bootcamp2023.db"
conn = sqlite3.connect("Bootcamp2023.db")
print(conn)


query='''create table donors(d_no int primary key,name text not null,age text not null, gender text,ph_no int,bld_grp text not null,qnty int not null,hm_ll float not null)'''


conn.execute(query)

