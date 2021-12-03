CREATE TABLE IF NOT EXISTS dwh.dim_province( pk_updateDate TIMESTAMP,pk_idProvincia SMALLINT,nationName VARCHAR(3),idRegione SMALLINT,provinciaShortName VARCHAR,PRIMARY KEY(pk_updateDate, pk_idProvincia));
CREATE TABLE IF NOT EXISTS dwh.dim_regioni( pk_updateDate TIMESTAMP,pk_idRegione SMALLINT,nationName VARCHAR(3),regioneName VARCHAR,PRIMARY KEY(pk_updateDate, pk_idRegione));
CREATE TABLE IF NOT EXISTS dwh.fac_total(pk_updateDate TIMESTAMP, msr_total INT);