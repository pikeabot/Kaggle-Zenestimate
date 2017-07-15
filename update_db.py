import psycopg2
import csv
import sys

# sudo -u postgres psql postgres

def update_tables():
  f = open('properties_2016.csv', 'rb')
  reader = csv.reader(f)
  for row in reader:
    #print row
    break
  for house in reader:
    command = """INSERT INTO homes(
                  parcelid, 
                  airconditioningtypeid, 
                  architecturalstyletypeid, 
                  basementsqft, 
                  bathroomcnt, 
                  bedroomcnt, 
                  buildingclasstypeid, 
                  buildingqualitytypeid, 
                  calculatedbathnbr, 
                  decktypeid, 
                  finishedfloor1squarefeet, 
                  calculatedfinishedsquarefeet, 
                  finishedsquarefeet12, 
                  finishedsquarefeet13, 
                  finishedsquarefeet25, 
                  finishedsquarefeet50, 
                  finishedsquarefeet6, 
                  fips, 
                  fireplacecnt, 
                  fullbathcnt, 
                  garagecarcnt, 
                  garagetotalsqft, 
                  hashottuborspa, 
                  heatingorsystemtypeid, 
                  latitude, 
                  longitude, 
                  lotsizesquarefeet, 
                  poolcnt, 
                  poolsizesum, 
                  pooltypeid10, 
                  pooltypeid2, 
                  pooltypeid7, 
                  propertycountylandusecode, 
                  propertylandusetypeid, 
                  propertyzoningdesc, 
                  rawcensustractandblock, 
                  regionidcity, 
                  regionidcounty, 
                  regionidneighborhood, 
                  regionidzip, 
                  roomcnt, 
                  storytypeid, 
                  threequarterbathnbr, 
                  typeconstructiontypeid, 
                  unitcnt, 
                  yardbuildingsqft17, 
                  yardbuildingsqft26, 
                  yearbuilt, 
                  numberofstories, 
                  fireplaceflag, 
                  structuretaxvaluedollarcnt, 
                  taxvaluedollarcnt, 
                  assessmentyear, 
                  landtaxvaluedollarcnt, 
                  taxamount, 
                  taxdelinquencyflag, 
                  taxdelinquencyyear, 
                  censustractandblock) 
                  VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s,  
                          %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
                          %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
                          %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
                          %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
                          %s, %s, %s, %s, %s, %s, %s, %s);
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
                  house[1],    #airconditioningtypeid INTEGER, 
                  house[2],    #architecturalstyletypeid INTEGER, 
                  house[3],    #basementsqft INTEGER, 
                  house[4],  #bathroomcnt DECIMAL,
                  house[5],    #bedroomcnt INTEGER,
                  house[6],    #buildingqualitytypeid INTEGER
                  house[7],    #buildingclasstypeid INTEGER,
                  house[8],  #calculatedbathnbr DECIMAL,
                  house[9],    #decktypeid INTEGER, 
                  house[10],   #threequarterbathnbr INTEGER,
                  house[11],   #finishedfloor1squarefeet INTEGER, 
                  house[12],   #calculatedfinishedsquarefeet INTEGER,
                  house[13],   #finishedsquarefeet6 INTEGER, 
                  house[14],   #finishedsquarefeet12 INTEGER,
                  house[15],   #finishedsquarefeet13 INTEGER,
                  house[16],   #finishedsquarefeet15 INTEGER,
                  house[17],   #finishedsquarefeet50 INTEGER,
                  house[18],   #fips INTEGER,
                  house[19],   #fireplacecnt INTEGER, 
                  house[20],   #fireplaceflag INTEGER,
                  house[21],   #fullbathcnt INTEGER, 
                  house[22],   #garagecarcnt INTEGER,
                  house[23],   #garagetotalsqft INTEGER, 
                  house[24],   #hashottuborspa INTEGER,
                  house[25],   #heatingorsystemtypeid INTEGER, 
                  house[26],   #latitude INTEGER, 
                  house[27],   #longitude INTEGER,
                  house[28],   #lotsizesquarefeet INTEGER, 
                  house[29],   #numberofstories INTEGER, 
                  house[30],   #poolcnt INTEGER, 
                  house[31],   #poolsizesum INTEGER,
                  house[32],   #pooltypeid10 INTEGER,
                  house[33],   #pooltype2id10 INTEGER
                  house[34],   #pooltypeid7 INTEGER, 
                  house[35],        #propertycountylandusecode VARCHAR(10),
                  house[36],   #propertylandusetypeid INTEGER,
                  house[37],        #propertyzoningdesc VARCHAR(10),
                  house[38], #rawcensustractandblock DECIMAL,
                  house[39],   #censustractandblock INTEGER,
                  house[40],   #regionidcounty INTEGER, 
                  house[41],   #regionidcity INTEGER, 
                  house[42],   #regionidzip INTEGER, 
                  house[43],   #regionidneighborhood INTEGER,
                  house[44],   #roomcnt INTEGER, 
                  house[45],   #storytypeid INTEGER,  
                  house[46],   #typeconstructiontypeid INTEGER, 
                  house[47],   #unitcnt INTEGER,
                  house[48],   #yardbuildingsqft17 INTEGER, 
                  house[49],   #yardbuildingsqft26 INTEGER, 
                  house[50],   #yearbuilt INTEGER,
                  house[51],   #taxvaluedollarcnt INTEGER, 
                  house[52],   #structuretaxvaluedollarcnt INTEGER, 
                  house[53],   #landtaxvaluedollarcnt INTEGER, 
                  house[54], #taxamount DECIMAL, 
                  house[55],   #assessmentyear INTEGER, 
                  house[56],        #taxdelinquencyflag VARCHAR(2), 
                  house[57]))  #taxdelinquencyyear INTEGER
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