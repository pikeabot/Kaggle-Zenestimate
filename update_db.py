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
    print house
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
                  finishedsquarefeet15, 
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
                          %s, %s, %s, %s, %s, %s, %s, %s, %s);
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

      for i in range(0, 58):
        if i not in [35, 37, 56]:
          if house[i]=='':
            if house[i] in [4, 8, 38, 54]:
              house=0.0
            else:
              house[i]=0
    except Exception as error:
      print ('here')
      print(error)
      sys.exit(1)
    try:
      cur.execute(command, (int(house[0]),
                  int(house[1]),    #airconditioningtypeid INTEGER, 
                  int(house[2]),    #architecturalstyletypeid INTEGER, 
                  int(house[3]),    #basementsqft INTEGER, 
                  float(house[4]),  #bathroomcnt DECIMAL,
                  int(house[5]),    #bedroomcnt INTEGER,
                  int(house[6]),    #buildingqualitytypeid INTEGER
                  int(house[7]),    #buildingclasstypeid INTEGER,
                  float(house[8]),  #calculatedbathnbr DECIMAL,
                  int(house[9]),    #decktypeid INTEGER, 
                  int(house[10]),   #threequarterbathnbr INTEGER,
                  int(house[11]),   #finishedfloor1squarefeet INTEGER, 
                  int(house[12]),   #calculatedfinishedsquarefeet INTEGER,
                  int(house[13]),   #finishedsquarefeet6 INTEGER, 
                  int(house[14]),   #finishedsquarefeet12 INTEGER,
                  int(house[15]),   #finishedsquarefeet13 INTEGER,
                  int(house[16]),   #finishedsquarefeet15 INTEGER,
                  int(house[17]),   #finishedsquarefeet50 INTEGER,
                  int(house[18]),   #fips INTEGER,
                  int(house[19]),   #fireplacecnt INTEGER, 
                  int(house[20]),   #fireplaceflag INTEGER,
                  int(house[21]),   #fullbathcnt INTEGER, 
                  int(house[22]),   #garagecarcnt INTEGER,
                  int(house[23]),   #garagetotalsqft INTEGER, 
                  int(house[24]),   #hashottuborspa INTEGER,
                  int(house[25]),   #heatingorsystemtypeid INTEGER, 
                  int(house[26]),   #latitude INTEGER, 
                  int(house[27]),   #longitude INTEGER,
                  int(house[28]),   #lotsizesquarefeet INTEGER, 
                  int(house[29]),   #numberofstories INTEGER, 
                  int(house[30]),   #parcelid INTEGER, 
                  int(house[31]),   #poolcnt INTEGER, 
                  int(house[32]),   #poolsizesum INTEGER,
                  int(house[33]),   #pooltypeid10 INTEGER,
                  int(house[34]),   #pooltypeid7 INTEGER, 
                  house[35],        #propertycountylandusecode VARCHAR(10),
                  int(house[36]),   #propertylandusetypeid INTEGER,
                  house[37],        #propertyzoningdesc VARCHAR(10),
                  float(house[38]), #rawcensustractandblock DECIMAL,
                  int(house[39]),   #censustractandblock INTEGER,
                  int(house[40]),   #regionidcounty INTEGER, 
                  int(house[41]),   #regionidcity INTEGER, 
                  int(house[42]),   #regionidzip INTEGER, 
                  int(house[43]),   #regionidneighborhood INTEGER,
                  int(house[44]),   #roomcnt INTEGER, 
                  int(house[45]),   #storytypeid INTEGER,  
                  int(house[46]),   #typeconstructiontypeid INTEGER, 
                  int(house[47]),   #unitcnt INTEGER,
                  int(house[48]),   #yardbuildingsqft17 INTEGER, 
                  int(house[49]),   #yardbuildingsqft26 INTEGER, 
                  int(house[50]),   #yearbuilt INTEGER,
                  int(house[51]),   #taxvaluedollarcnt INTEGER, 
                  int(house[52]),   #structuretaxvaluedollarcnt INTEGER, 
                  int(house[53]),   #landtaxvaluedollarcnt INTEGER, 
                  float(house[54]), #taxamount DECIMAL, 
                  int(house[55]),   #assessmentyear INTEGER, 
                  house[56],        #taxdelinquencyflag VARCHAR(2), 
                  int(house[57])))  #taxdelinquencyyear INTEGER
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