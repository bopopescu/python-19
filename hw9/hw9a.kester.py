#---------------------------------------------------------
# April Dawn Kester
# akester@ischool.berkeley.edu
# Homework #8
# October 30, 2014
# SQL File A
#---------------------------------------------------------

import sqlite3

conn = sqlite3.connect("my_db.db")
lol = conn.cursor()

lol.execute("""drop table my_db;""")

#names, phone numbers, and address of four made-up people
lol.execute("""
    create table my_db (
        first_name character varying(50),
        last_name character varying(50),
        phone character varying(50),
        address character varying(50),
        city character varying(50),
        state character varying(50),
        postal_code character varying(50)
    );
    """)

data = [("Bob", "Smith", "477-9093", "203 Koshland Way", "Santa Cruz", "CA", "95064"),
("Susan", "Smith", "477-9093", "203 Koshland Way", "Santa Cruz", "CA", "95064"),
("Chris", "Rogers", "513-3340", "605 Ohlone Ave #618", "Albany", "CA", "94706"),
("Yorik", "Aguilar", "476-5555", "1315 Rodriguez", "Santa Cruz", "CA", "95062"),
        ]
lol.executemany('insert into my_db values (?, ?, ?, ?, ?, ?, ?)', data)

conn.commit()

#grabs the address of everyone whose name begins with a letter between M and Z inclusive
for row in lol.execute("""
    select address, city, state, postal_code
    from my_db
    where first_name>="M";
    """):
        
    print row

conn.close()

