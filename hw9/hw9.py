#homework 9


import sqlite3

conn = sqlite3.connect("Chinook.db")
cur = conn.cursor()

#for row in cur.execute('Select * from Album;'):
#print row

for row in cur.execute('Select Track.Name, Track.Milliseconds from Track, MediaType where Track.TrackId = MediaType.MediaTypeId and MediaType.Name = "Protected MPEG-4 video file" Order by Track.Milliseconds DESC Limit 1;'):
    print row

#Select Artist.Name
#From Artist, Album
#Where Artist.ArtistID = Album.ArtistID And Album.Title = "Balls to the Wall";



