from sqlalchemy import engine as sqlA

db_name = 'DWH_COVID'
db_user = 'sa_etl'
db_pass = 'password'
db_host = '172.24.0.2'
db_port = '5432'

def connection():
    # Connecto to the database
    db_string = 'postgres://{}:{}@{}:{}/{}'.format(db_user, db_pass, db_host, db_port, db_name)
    engine = sqlA.create_engine(db_string, pool_size=5, max_overflow=0)
    db = engine.connect()
    return db