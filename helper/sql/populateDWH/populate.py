from numpy import void0

#Populate dimensions
def populateDimensions(conn, dataset):
    for row in dataset.itertuples():
        conn.execute('''
                    INSERT INTO dwh.dim_regioni (pk_updateDate, pk_idRegione, nationName, regioneName)
                    VALUES (?,?,?,?)
                    ''',
                    row.data, 
                    row.codice_regione,
                    row.stato 
                    )

    return void0