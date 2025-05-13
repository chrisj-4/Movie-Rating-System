import sqlite3
import time

#conn = sqlite3.connect('movieratings.db') 
#cursor = conn.cursor()

#start = time.time()
#cursor.execute("SELECT * FROM MovieRatings WHERE Rating = 5")
#results = cursor.fetchall()
#for row in results:
 #   print(row)
#end = time.time()

#print("Query took:", end - start, "seconds")
#conn.close()



# Simulate 100 real-time feedback inserts
conn = sqlite3.connect('movieratings.db') 
cur = conn.cursor()

start_time = time.time()
for i in range(100):
    cur.execute("INSERT INTO MovieRatings (UserName, MovieTitle, Rating, ReviewText) VALUES (?, ?, ?, ?)",
                (f'user{i}', 'The Batman', 4, 'Testing insert speed'))
conn.commit()
print("Insert 100 ratings time:", time.time() - start_time, "seconds")

conn.close()