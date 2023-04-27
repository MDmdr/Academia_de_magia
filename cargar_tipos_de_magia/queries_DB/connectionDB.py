import sqlalchemy
from sqlalchemy import create_engine, MetaData, Table, text

# CONFIG LOCAL
host = "localhost:3306"
user = "root"
password = "54321bd"
DataBase = 'bd_reino_del_trevol'

# CONFIGURACION EXTERNA
# host = ""
# user = ""
# password = ""
# DataBase = ''

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