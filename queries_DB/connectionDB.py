import sqlalchemy
from sqlalchemy import create_engine, MetaData, Table, text

# CONFIG LOCAL
host = "localhost:3306"
user = "root"
password = "54321bd"
DataBase = 't2_monte_xan'

# CONFIG monte_xanic EXTERNA
# host = "montexanic.cacvh5hnp5ks.us-east-2.rds.amazonaws.com"
# user = "ramon"
# password = "R4m0.n322"
# DataBase = 'monte_xanic'

def conection():
    engine = create_engine(
        'mysql+pymysql://'+user+':'+password+'@'+host+'/'+DataBase,
        # echo=True
        echo=False
    )
    return engine.connect() # regresa una conexion a Base de Datos

def get_DataBase():
    return DataBase
# ----------------------------------------