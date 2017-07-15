import psycopg2
#from config import config

# sudo -u postgres psql postgres
# \c zillowdb

def create_tables():
  """ create tables in the PostgreSQL database"""
  command = """
    CREATE TABLE IF NOT EXISTS homes (
      house_id SERIAL PRIMARY KEY,  
      airconditioningtypeid VARCHAR(25),            
      architecturalstyletypeid VARCHAR(25),  
      basementsqft VARCHAR(25), 
      bathroomcnt VARCHAR(25),
      bedroomcnt VARCHAR(25), 
      buildingqualitytypeid VARCHAR(25), 
      buildingclasstypeid VARCHAR(25), 
      calculatedbathnbr VARCHAR(25),
      decktypeid VARCHAR(25), 
      threequarterbathnbr VARCHAR(25), 
      finishedfloor1squarefeet VARCHAR(25), 
      calculatedfinishedsquarefeet VARCHAR(25), 
      finishedsquarefeet6 VARCHAR(25), 
      finishedsquarefeet12 VARCHAR(25), 
      finishedsquarefeet13 VARCHAR(25), 
      finishedsquarefeet25 VARCHAR(25), 
      finishedsquarefeet50 VARCHAR(25), 
      fips VARCHAR(25), 
      fireplacecnt VARCHAR(25), 
      fireplaceflag VARCHAR(25), 
      fullbathcnt VARCHAR(25), 
      garagecarcnt VARCHAR(25), 
      garagetotalsqft VARCHAR(25), 
      hashottuborspa VARCHAR(25), 
      heatingorsystemtypeid VARCHAR(25), 
      latitude VARCHAR(25), 
      longitude VARCHAR(25), 
      lotsizesquarefeet VARCHAR(25), 
      numberofstories VARCHAR(25), 
      parcelid VARCHAR(25), 
      poolcnt VARCHAR(25), 
      poolsizesum VARCHAR(25), 
      pooltypeid10 VARCHAR(25), 
      pooltypeid2 VARCHAR(25), 
      pooltypeid7 VARCHAR(25), 
      propertycountylandusecode VARCHAR(25),
      propertylandusetypeid VARCHAR(25), 
      propertyzoningdesc VARCHAR(25),
      rawcensustractandblock VARCHAR(25),
      censustractandblock VARCHAR(25), 
      regionidcounty VARCHAR(25), 
      regionidcity VARCHAR(25), 
      regionidzip VARCHAR(25), 
      regionidneighborhood VARCHAR(25), 
      roomcnt VARCHAR(25),  
      storytypeid VARCHAR(25),  
      typeconstructiontypeid VARCHAR(25), 
      unitcnt VARCHAR(25), 
      yardbuildingsqft17 VARCHAR(25), 
      yardbuildingsqft26 VARCHAR(25), 
      yearbuilt VARCHAR(25), 
      taxvaluedollarcnt VARCHAR(25), 
      structuretaxvaluedollarcnt VARCHAR(25), 
      landtaxvaluedollarcnt VARCHAR(25), 
      taxamount VARCHAR(25), 
      assessmentyear VARCHAR(25), 
      taxdelinquencyflag VARCHAR(2), 
      taxdelinquencyyear VARCHAR(25)
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