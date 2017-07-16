import plotly
import psycopg2
import geoplotlib


try:
  conn = psycopg2.connect("dbname='zillowdb' user='zillow' host='localhost' password='dbpass'")
except:
  print "I am unable to connect to the database."
    
cur = conn.cursor()
try:
  cur.execute("""SELECT latitude, longitude FROM homes WHERE house_id<100;""")

except (Exception, psycopg2.DatabaseError) as error:
   print(error)

coords = cur.fetchall()

thedata = {'lat': [float(i[0])/1000000 for i in coords], 'lon': [float(j[1])/1000000 for j in coords]}

# close communication with the PostgreSQL database server
cur.close()

# display geographical map
geoplotlib.dot(thedata)
geoplotlib.show()