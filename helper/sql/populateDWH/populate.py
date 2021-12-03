from multiprocessing import Process

#Populate dimensions
def populateRegionDimension(conn, dataset):
    conn.execute('''TRUNCATE TABLE dwh.dim_regioni;''')
    for row in dataset.itertuples():
        conn.execute('''
                    INSERT INTO dwh.dim_regioni (pk_updateDate, pk_idRegione, nationName, regioneName)
                    VALUES (%s,%s,%s,%s)
                    ''',
                    row.data, 
                    row.codice_regione,
                    row.stato,
                    row.denominazione_regione
                    )

def populateProvinceDimension(conn, dataset):
    conn.execute('''TRUNCATE TABLE dwh.dim_province;''')
    for row in dataset.itertuples():
        conn.execute('''
                    INSERT INTO dwh.dim_province (pk_updateDate, pk_idProvincia, nationName, idRegione, provinciaShortName)
                    VALUES (%s,%s,%s,%s,%s)
                    ''',
                    row.data, 
                    row.codice_provincia,
                    row.stato,
                    row.codice_regione,
                    row.sigla_provincia
                    ) 
                    
#Executing in parallel
def multiprocess(*function):
    for process in function:
        p = Process(target= process)
        p.start()

def mainPopulate(conn, region, province):
    multiprocess(populateProvinceDimension(conn, province), 
                 populateRegionDimension(conn, region)
                )
