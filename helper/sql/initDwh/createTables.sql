--Dimension tables
CREATE TABLE IF NOT EXISTS dwh.dim_province( pk_updateDate DATE,
                                             pk_idProvincia SMALLINT,
                                             nationName VARCHAR(3),
                                             idRegione SMALLINT,
                                             provinciaShortName VARCHAR,
                                             PRIMARY KEY(pk_updateDate, pk_idProvincia)
                                            );

CREATE TABLE IF NOT EXISTS dwh.dim_regioni( pk_updateDate DATE,
                                            pk_idRegione SMALLINT,
                                            nationName VARCHAR(3),
                                            regioneName VARCHAR,
                                            PRIMARY KEY(pk_updateDate, pk_idRegione)
                                            );

--Fac tables
CREATE TABLE IF NOT EXISTS dwh.fac_total(msr_total INT);