import psycopg2
import csv
import sys

# sudo -u postgres psql postgres

def update_tables():
  f = open('train_2016_v2.csv', 'rb')
  reader = csv.reader(f)
  for row in reader:
    #print row
    break
  for house in reader:
    command = """INSERT INTO train(
                  parcelid, 
                  logerror,  
                  transactiondate) 
                  VALUES (%s, %s, %s);
             """
    conn = None
    try:
      # read the connection parameters
      #params = config()
      # connect to the PostgreSQL server
      conn = psycopg2.connect("dbname='zillowdb' user='zillow' host='localhost' password='dbpass'")
      cur = conn.cursor()
      # create table one by one
      #for command in commands:
      print house[0]
      cur.execute(command, 
                  (house[0],  #parcelid
                  float(house[1]),    #airconditioningtypeid INTEGER, 
                  house[2]))    #architecturalstyletypeid INTEGER, 
      # close communication with the PostgreSQL database server
      cur.close()
      # commit the changes
      conn.commit()
      
    except (Exception, psycopg2.DatabaseError) as error:
      print house[0]
      print(error)
      sys.exit(1)
    finally:
      if conn is not None:
          conn.close()
  f.close()

if __name__ == '__main__':
   update_tables()