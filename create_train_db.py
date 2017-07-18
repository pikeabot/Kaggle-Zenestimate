import psycopg2
#from config import config

# sudo -u postgres psql postgres
# \c zillowdb

def create_tables():
  """ create tables in the PostgreSQL database"""
  command = """
    CREATE TABLE IF NOT EXISTS train (
      parcelid VARCHAR(25),  
      logerror REAL,
      transactiondate DATE, 
      FOREIGN KEY (parcelid) REFERENCES homes (parcelid)
    )"""
    
  conn = None
  try:
    # read the connection parameters
    #params = config()
    # connect to the PostgreSQL server
    conn = psycopg2.connect("dbname='zillowdb' user='zillow' host='localhost' password='dbpass'")
    cur = conn.cursor()
    # create table one by one
    #for command in commands:
    print command
    cur.execute(command)
    # close communication with the PostgreSQL database server
    cur.close()
    # commit the changes
    conn.commit()
  except (Exception, psycopg2.DatabaseError) as error:
     print(error)
  finally:
    if conn is not None:
        conn.close()

 
if __name__ == '__main__':
   create_tables()