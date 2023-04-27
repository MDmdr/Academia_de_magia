import sqlalchemy
from sqlalchemy import create_engine, MetaData, Table, text # SE REQUIERE TEXT


from datetime import datetime
import uuid
def getDate():  
    now = datetime.now()
    # now.year  # now.month  # now.day
    return str(now.year)+"/"+str(now.month)+"/"+str(now.day)
def getHour():  
    now = datetime.now()    
    return str(now.hour)+":"+str(now.minute)+":"+str(now.second)
def getUid():    
    return str(uuid.uuid4().hex)

# -----------------------------------------
from queries_DB import connectionDB
def connection():    
    return connectionDB.conection()

DataBase = connectionDB.get_DataBase();
# ------------------------------------------
# CRUD'S
#----------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------

