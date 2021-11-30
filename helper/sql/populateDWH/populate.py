from numpy import void0
import multiprocessing as mp

#Prepare multiprocessing
pool = mp.Pool(mp.cpu_count())

def mainPopulate(conn, dataset):
    pool.map(populateProvinceDimension(conn,dataset),populateRegionDimension(conn,dataset) )
    return void0

#Populate dimensions
def populateRegionDimension(conn, dataset):
    for row in dataset.itertuples():
        conn.execute('''
                    INSERT INTO dwh.dim_regioni (pk_updateDate, pk_idRegione, nationName, regioneName)
                    VALUES (?,?,?,?)
                    ''',
                    row.data, 
                    row.codice_regione,
                    row.stato,
                    row.denominazione_regione
                    )

    return void0

def populateProvinceDimension(conn, dataset):
    for row in dataset.itertuples():
        conn.execute('''
                    INSERT INTO dwh.dim_province (pk_updateDate, pk_idProvincia, nationName, idRegione, provinciaShortName)
                    VALUES (?,?,?,?)
                    ''',
                    row.data, 
                    row.codice_provincia,
                    row.stato,
                    row.codiceRegione,
                    row.sigla_provincia
                    )
    return void0

print