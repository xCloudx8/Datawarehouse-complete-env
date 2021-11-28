#Check if tables are create if not recreate
def initialize(conn):
    #Create schema
    with open('helper/sql/initDwh/createSchema.sql') as f:
        lines = f.readlines()
    
    for line in lines:
        conn.execute(line)

    #Create tables
    with open('helper/sql/initDwh/createTables.sql') as f:
        lines = f.readlines()
    
    for line in lines:
        conn.execute(line)
    