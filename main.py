#Starter file for system
from helper import connector
from helper.sql.initDwh import checkTable
from data import getData
from helper.sql.populateDWH import populate

#Connect to DB
conn = connector.connection()
res = conn.execute("SELECT 'Connected'")

#Initialize DWH
checkTable.initialize(conn)

#GetUpdatedData
region = getData.getRegioni_dataset()
province = getData.getProvince_dataset()

#Populate dimension tables
populate.populateDimensions(conn, region)

#Populate fact tables


#Build datamarts


#Close connection
conn.close()
print("End of process")