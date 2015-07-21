#---------------------------------------------------------
# April Dawn Kester
# akester@ischool.berkeley.edu
# Homework #8
# October 30, 2014
# SQL File C
#---------------------------------------------------------



import sqlite3
from ggplot import *
import pandas

conn = sqlite3.connect('track_metadata.db')

myData = pandas.read_sql_query("""select year, count(*) from songs where artist_name = "Rick Astley" and year!= 0 group by year;""", conn)

print myData

print ggplot(aes(x='year', y='count(*)'), data=myData) + \
    geom_bar(stat = "bar") + \
    scale_y_continuous(breaks=(5,10,15,20,30), labels=("5", "10", "15", "20", "30"))

conn.close()
