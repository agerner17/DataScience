import sqlite3 as lite
import pandas as pd
import collections

cities = (('New York City', 'NY'),
	('Las Vegas', 'NV'), 
	('Atlanta', 'GA'), 
	('Chicago', 'IL'), 
	('Miami', 'FL'), 
	('Dallas', 'TX'), 
	('Seattle', 'OR'), 
	('San Francisco', 'CA'), 
	('Los Angeles', 'CA'))


weather = (('New York City' , 2013, 'July', 'January', 62),
	('Chicago', 2013, 'July', 'January', 59), 
	('Atlanta', 2013, 'August', 'January', 90), 
	('Miami', 2013, 'August', 'January', 84), 
	('Dallas', 2013, 'July', 'January', 77), 
	('Seattle', 2013, 'July', 'January', 61), 
	('San Francisco', 2013, 'September', 'December', 64), 
	('Los Angeles', 2013, 'September', 'December', 75))

con = lite.connect('getting_started.db')

citiesList = []
statesList = []
# Inserting rows by passing values directly to `execute()`
with con:

	cur = con.cursor()
	cur.execute("DROP TABLE if exists cities")
	cur.execute("DROP TABLE if exists weather")
	cur.execute("CREATE TABLE cities(name text, state text)")
	cur.execute("create table weather(city text, year integer, warmMonth text, coldMonth text, averageMonth integer)")
	cur.executemany("INSERT INTO cities VALUES(?,?)", cities)
	cur.executemany("INSERT INTO weather VALUES(?,?,?,?,?)", weather)

	cur.execute("select name, state, warmMonth FROM cities INNER JOIN weather On name = city where warmMonth = 'July'")

  	rows = cur.fetchall()
  	
  	cols = [desc[0] for desc in cur.description]

  	ab = pd.DataFrame(rows, columns=cols)
  	
  	for line in rows:
  		citiesList.append(line[0])
  		statesList.append(line[1])
  	

  	print("The cities that are warmest in July are: " + citiesList[0] + ", " +statesList[0]+ ", "+citiesList[1]+ ", "+statesList[1]+", "+citiesList[2]+ ", "+statesList[2]+ ", and "+citiesList[3]+ ", "+statesList[3]+ ".")
  		




  		


	
	