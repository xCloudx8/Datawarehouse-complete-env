from multiprocessing import Process

#Populate dimensions
def populateRegionDimension(conn, dataset):
    for row in dataset.itertuples():
        conn.execute('''
                    INSERT INTO dwh.dim_regioni (pk_updateDate, pk_idRegione, nationName, regioneName)
                    VALUES (%s,%s,%s,%s)
                    ON CONFLICT (pk_updateDate, pk_idRegione) DO NOTHING;
                    ''',
                    row.data, 
                    row.codice_regione,
                    row.stato,
                    row.denominazione_regione
                    )

def populateProvinceDimension(conn, dataset):
    for row in dataset.itertuples():
        conn.execute('''
                    INSERT INTO dwh.dim_province (pk_updateDate, pk_idProvincia, nationName, idRegione, provinciaShortName)
                    VALUES (%s,%s,%s,%s,%s)
                    ON CONFLICT (pk_updateDate, pk_idProvincia) DO NOTHING;
                    ''',
                    row.data, 
                    row.codice_provincia,
                    row.stato,
                    row.codice_regione,
                    row.sigla_provincia
                    ) 

def populateFacProvince(conn, datasetProvince):
    for row in datasetProvince.itertuples():
        conn.execute('''
                    INSERT INTO dwh.fac_totalCasesProvince (pk_updateDate,idProvincia, msr_totalCasesProvince)
                    VALUES (%s,%s,%s)
                    ON CONFLICT (pk_updateDate, idProvincia) DO NOTHING;

                    ''',
                    row.data, 
                    row.codice_provincia,
                    row.totale_casi
                    ) 

def populateFacRegioni(conn, datasetRegioni):
    for row in datasetRegioni.itertuples():
        conn.execute('''
                    INSERT INTO dwh.fac_totalCasesRegioni (pk_updateDate,idRegione, msr_totalCasesRegion)
                    VALUES (%s,%s,%s)
                    ON CONFLICT (pk_updateDate, idRegione) DO NOTHING;
                    ''',
                    row.data, 
                    row.codice_regione,
                    row.totale_casi
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
    populateFacProvince(conn,province)
    populateFacRegioni(conn,region)

