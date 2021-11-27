#Check if tables are create if not recreate
def checkTables(conn):
    #Create schema
    with open('helper/sql/createSchema.sql') as f:
        lines = f.readlines()
    
    for line in lines:
        conn.execute(line)

    #Create tables
    with open('helper/sql/creteTables.sql') as f:
        lines = f.readlines()
    
    for line in lines:
        conn.execute(line)
    