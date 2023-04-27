

# CARGAR DATA

# ----------------------------------------------------------------------------
import sqlalchemy
from sqlalchemy import create_engine, MetaData, Table, text # SE REQUIERE TEXT
# ----------------------------------------------------------------------------
from queries_DB import connectionDB
def connection():    
    return connectionDB.conection()
DataBase = connectionDB.get_DataBase();
# ----------------------------------------------------------------------------
# ----------------------------
# ----------------------------
def file_read(route_And_File):
	parrafo_f = ""		
	try:
		f = open (route_And_File,'r') # archivo-entrada
		parrafo_f = f.read()
		f.close()
	except Exception as e:
		print("ERROR AL LEER ARCHIVO:",str(e) )
		parrafo_f = "NULL"
	return parrafo_f
# DEBUELVE UN ARRAY CON LAS LINEAS
def get_lines(routeAndFile):
	texto = file_read(routeAndFile)
	texto = texto.split("\n")
	return texto


def save_magic_type(conn,magic_type):
	# -----------------------------------------------
    text1 = "insert INTO  "+DataBase+".tipos_de_magia (nombre) VALUES ('"+magic_type+"');"
    # print(text1)    
    sql_text = text( text1 )
    result = conn.execute(sql_text)
    # -----------------------------------------------
    print("SAVE ONE REGISTER IN DATA BASE: "+str(magic_type) )
    return ""

# -----------------------------------------------------------------------------------

def funcion_principal():
	# leer Data
	routeAndFile = "Tipos de Magia.csv"
	data = get_lines(routeAndFile)
	# print(data)
	# recorrer data en la columna
	i = 0
	conn = connection()
	for item in data:
		# print(item)
		if item != "":			
			try:
				item = item.replace(",","")
				save_magic_type(conn,item)
				i = i + 1
			except Exception as e:
				print("Error al guardar:"+str(item) )
	conn.close()
	print(str(i) + " REGISTROS GUARDADOS")
	return True

funcion_principal()


