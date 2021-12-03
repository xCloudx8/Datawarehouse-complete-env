def checkTime(conn):
    #check tables existing
    table_list = []
    table = conn.execute('''
        SELECT tablename 
        FROM pg_catalog.pg_tables 
        WHERE schemaname='dwh';
    
    ''')
    for tbl in table:
        table_list.append(tbl[0])

    list = []
    for t in table_list:
        time = conn.execute('''
            SELECT MAX(pk_updateDate)
            FROM dwh.'''+ t + ''';
        ''')
    list.append(time)
    dateTime = min(list)
    
    for t in dateTime:
        return t[0]