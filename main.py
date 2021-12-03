#Starter file for system
from data import getData
from helper import connector
from datetime import datetime, timedelta
from helper.sql.initDwh import checkTable
from helper.sql.populateDWH import populate
from helper.sql.lastUpdate import lastUpdate

#Connect to DB
conn = connector.connection()
res = conn.execute("SELECT 'Connected'")

#Initialize DWH
checkTable.initialize(conn)

#CheckLastUpdateDate
time = lastUpdate.checkTime(conn)

if time is None:
    time = datetime.strptime('20200224', '%Y%m%d') #Start date for collecting data
else:
    time = datetime.strptime(str(time), '%Y-%m-%d %H:%M:%S')
    time = time.strftime('%Y%m%d')

today = datetime.strptime(datetime.today().strftime('%Y%m%d'), '%Y%m%d')
today -= timedelta(days=1)
today = today.strftime('%Y%m%d')

while time != today:
    print(time, today)
    #GetUpdatedData
    region = getData.getRegioni_dataset(time)
    province = getData.getProvince_dataset(time)

    #Populate dimension tables
    populate.mainPopulate(conn, region, province)

    #Populate fact tables


    #Build datamarts

    time+=timedelta(days=1)

#Close connection
conn.close()
print("End of process")