#---------------------------------------------------------
# April Dawn Kester
# akester@ischool.berkeley.edu
# Homework #8
# October 30, 2014
# SQL File B
#---------------------------------------------------------

import sqlite3
conn = sqlite3.connect('track_metadata.db')
lol = conn.cursor()


for row in lol.execute("""
    select title
    from songs
    where artist_name = "The Beatles";
    """):
    print row

conn.close()