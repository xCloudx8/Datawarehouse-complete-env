#Starter file for system
from helper import connector
from helper.sql import checkTable

#Connect to DB
conn = connector.connection()
res = conn.execute("SELECT 'Connected'")

#Check if db is not empty if yes prepare DB
checkTable.checkTables(conn)