import psycopg2
#from config import config

# sudo -u postgres psql postgres

def create_tables():
  """ create tables in the PostgreSQL database"""
  command = """
    CREATE TABLE IF NOT EXISTS homes (
      house_id SERIAL PRIMARY KEY,
      airconditioningtypeid INTEGER, 
      architecturalstyletypeid INTEGER,  
      basementsqft INTEGER, 
      bathroomcnt DECIMAL,
      bedroomcnt INTEGER, 
      buildingqualitytypeid INTEGER, 
      buildingclasstypeid INTEGER, 
      calculatedbathnbr DECIMAL,
      decktypeid INTEGER, 
      threequarterbathnbr INTEGER, 
      finishedfloor1squarefeet INTEGER, 
      calculatedfinishedsquarefeet INTEGER, 
      finishedsquarefeet6 INTEGER, 
      finishedsquarefeet12 INTEGER, 
      finishedsquarefeet13 INTEGER, 
      finishedsquarefeet15 INTEGER, 
      finishedsquarefeet50 INTEGER, 
      fips INTEGER, 
      fireplacecnt INTEGER, 
      fireplaceflag INTEGER, 
      fullbathcnt INTEGER, 
      garagecarcnt INTEGER, 
      garagetotalsqft INTEGER, 
      hashottuborspa INTEGER, 
      heatingorsystemtypeid INTEGER, 
      latitude INTEGER, 
      longitude INTEGER, 
      lotsizesquarefeet INTEGER, 
      numberofstories INTEGER, 
      parcelid INTEGER, 
      poolcnt INTEGER, 
      poolsizesum INTEGER, 
      pooltypeid10 INTEGER, 
      pooltypeid2 INTEGER, 
      pooltypeid7 INTEGER, 
      propertycountylandusecode VARCHAR(10),
      propertylandusetypeid INTEGER, 
      propertyzoningdesc VARCHAR(10),
      rawcensustractandblock DECIMAL,
      censustractandblock INTEGER, 
      regionidcounty INTEGER, 
      regionidcity INTEGER, 
      regionidzip INTEGER, 
      regionidneighborhood INTEGER, 
      roomcnt INTEGER,  
      storytypeid INTEGER,  
      typeconstructiontypeid INTEGER, 
      unitcnt INTEGER, 
      yardbuildingsqft17 INTEGER, 
      yardbuildingsqft26 INTEGER, 
      yearbuilt INTEGER, 
      taxvaluedollarcnt INTEGER, 
      structuretaxvaluedollarcnt INTEGER, 
      landtaxvaluedollarcnt INTEGER, 
      taxamount DECIMAL, 
      assessmentyear INTEGER, 
      taxdelinquencyflag VARCHAR(2), 
      taxdelinquencyyear INTEGER
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