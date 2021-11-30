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

#CheckLastUpdateDate


#GetUpdatedData
time = '20200224'
region = getData.getRegioni_dataset(time)
province = getData.getProvince_dataset(time)

#Populate dimension tables
populate.mainPopulate(conn, region)

#Populate fact tables


#Build datamarts


#Close connection
conn.close()
print("End of process")