table_list = ['dwh.dim_regione', 'dwh.dim_province']

def updateTime(conn):
    list = []
    for t in table_list:
        time = conn.execute('''
            SELECT MAX(pk_updateDate)
            FROM '''+ t + ''';
        ''')
    list.append(time)