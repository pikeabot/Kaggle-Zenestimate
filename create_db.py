import psycopg2
#from config import config

# sudo -u postgres psql postgres
# \c zillowdb

def create_tables():
  """ create tables in the PostgreSQL database"""
  command = """
    CREATE TABLE IF NOT EXISTS homes (
      house_id SERIAL PRIMARY KEY,
      airconditioningtypeid VARCHAR(15), 
      architecturalstyletypeid VARCHAR(15),  
      basementsqft VARCHAR(15), 
      bathroomcnt VARCHAR(15),
      bedroomcnt VARCHAR(15), 
      buildingqualitytypeid VARCHAR(15), 
      buildingclasstypeid VARCHAR(15), 
      calculatedbathnbr VARCHAR(15),
      decktypeid VARCHAR(15), 
      threequarterbathnbr VARCHAR(15), 
      finishedfloor1squarefeet VARCHAR(15), 
      calculatedfinishedsquarefeet VARCHAR(15), 
      finishedsquarefeet6 VARCHAR(15), 
      finishedsquarefeet12 VARCHAR(15), 
      finishedsquarefeet13 VARCHAR(15), 
      finishedsquarefeet15 VARCHAR(15), 
      finishedsquarefeet50 VARCHAR(15), 
      fips VARCHAR(15), 
      fireplacecnt VARCHAR(15), 
      fireplaceflag VARCHAR(15), 
      fullbathcnt VARCHAR(15), 
      garagecarcnt VARCHAR(15), 
      garagetotalsqft VARCHAR(15), 
      hashottuborspa VARCHAR(15), 
      heatingorsystemtypeid VARCHAR(15), 
      latitude VARCHAR(15), 
      longitude VARCHAR(15), 
      lotsizesquarefeet VARCHAR(15), 
      numberofstories VARCHAR(15), 
      parcelid VARCHAR(15), 
      poolcnt VARCHAR(15), 
      poolsizesum VARCHAR(15), 
      pooltypeid10 VARCHAR(15), 
      pooltypeid2 VARCHAR(15), 
      pooltypeid7 VARCHAR(15), 
      propertycountylandusecode VARCHAR(15),
      propertylandusetypeid VARCHAR(15), 
      propertyzoningdesc VARCHAR(15),
      rawcensustractandblock VARCHAR(15),
      censustractandblock VARCHAR(15), 
      regionidcounty VARCHAR(15), 
      regionidcity VARCHAR(15), 
      regionidzip VARCHAR(15), 
      regionidneighborhood VARCHAR(15), 
      roomcnt VARCHAR(15),  
      storytypeid VARCHAR(15),  
      typeconstructiontypeid VARCHAR(15), 
      unitcnt VARCHAR(15), 
      yardbuildingsqft17 VARCHAR(15), 
      yardbuildingsqft26 VARCHAR(15), 
      yearbuilt VARCHAR(15), 
      taxvaluedollarcnt VARCHAR(15), 
      structuretaxvaluedollarcnt VARCHAR(15), 
      landtaxvaluedollarcnt VARCHAR(15), 
      taxamount VARCHAR(15), 
      assessmentyear VARCHAR(15), 
      taxdelinquencyflag VARCHAR(2), 
      taxdelinquencyyear VARCHAR(15)
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