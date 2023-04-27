from flask import Flask, url_for, render_template, request, redirect, session
from flask_sqlalchemy import SQLAlchemy
# from flask import create_app
# app = create_app()

# CONFIG LOCAL
host = "localhost:3306"
user = "root"
password = "54321bd"
DataBase = 'bd_reino_del_trevol'

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://'+user+':'+password+'@'+host+'/'+DataBase
db = SQLAlchemy(app)

import random
import json
# ----------------------------------------------------------------------------
import sqlalchemy
from sqlalchemy import create_engine, MetaData, Table, text # SE REQUIERE TEXT
# ----------------------------------------------------------------------------
from queries_DB import connectionDB
def connection():    
    return connectionDB.conection()
DataBase = connectionDB.get_DataBase();
# ----------------------------------------------------------------------------

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))

    def __init__(self, username, password):
        self.username = username
        self.password = password


@app.route('/', methods=['GET'])
def index():
    if session.get('logged_in'):
        return render_template('home.html')
    else:
        return render_template('index.html', message="Hello!")


@app.route('/register/', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        try:
            db.session.add(User(username=request.form['username'], password=request.form['password']))
            db.session.commit()
            return redirect(url_for('login'))
        except:
            return render_template('index.html', message="User Already Exists")
    else:
        return render_template('register.html')


@app.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        u = request.form['username']
        p = request.form['password']
        data = User.query.filter_by(username=u, password=p).first()
        if data is not None:
            session['logged_in'] = True
            session['username'] = u
            return redirect(url_for('index'))
        return render_template('index.html', message="Incorrect Details")


@app.route('/logout', methods=['GET', 'POST'])
def logout():
    session['logged_in'] = False
    return redirect(url_for('index'))

# ------------------------------------------------------
# registro de solicitudes
@app.route('/registrar_solicitud/', methods=['GET','POST'])
def registrar_solicitud():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        if session.get('logged_in'):
            return render_template('registrar_solicitud.html',mensage_general="")
        else:
            return render_template('index.html', message="Hello!")
        # return render_template('index.html', message="Incorrect Details")

@app.route('/registrar_solicitud_de_estudiante/', methods=['GET','POST'])
def registrar_solicitud_de_estudiante():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        if session.get('logged_in'):            
            nombre = request.form['Nombre']
            apellido = request.form['Apellido']
            identificacion = request.form['Identificacion']
            edad = request.form['Edad']
            afinidad_magia = request.form['Afinidad_magia']
            # print(nombre)
            # print(apellido)
            # print(identificacion)
            # print(edad)
            # print(afinidad_magia)
            # print("sesion ¿?:")
            # print(session)           

            # Validar datos
            resultado = VALIDAR.validar_datos(nombre,apellido,identificacion,edad,afinidad_magia)
            if resultado == True:
                # asignar grimorio
                grimorio = grimorios.obtener_grimorio()
                grimorio = grimorios.obtener_categoria(grimorio)
                print("grimorio:"+grimorio)
                # guardar registro
                aux = guardar.guardar_registro(nombre,apellido,identificacion,edad,afinidad_magia,grimorio)
                if aux == True:
                    return render_template('registro_exitoso.html',mensage_general=grimorio)
                else:
                    return render_template('registrar_solicitud.html',mensage_general="Error al guardar, intetelo de nuevo.")
                
            else:                
                return render_template('registrar_solicitud.html',mensage_general=resultado+" SOLICITUD CANCELADA")                                  
            # ---
        else:
            return render_template('index.html', message="Vienvenido")
    return render_template('index.html', message="")
# ------------------------------------------------------
class guardar:
    def guardar_registro(nombre,apellido,identificacion,edad,afinidad_magia,grimorio):        
        try:
            conn = connection()
            # -----------------------------------------------
            text1 = "insert INTO  "+DataBase+".solicitudes (nombre,apellido,identificacion,edad,afinidad_magia,grimorio,estatus,datetime) VALUES ('"+nombre+"','"+apellido+"','"+identificacion+"',"+str(edad)+",'"+afinidad_magia+"','"+grimorio+"', 1, NOW() );"
            # print(text1)    
            sql_text = text( text1 )
            result = conn.execute(sql_text)
            # -----------------------------------------------
            conn.close()
        except Exception as e:
            return False
        return True
class VALIDAR:
    def validar_datos(nombre,apellido,identificacion,edad,afinidad_magia):
        resultado = ""    
        if validar_solicitud.validar_nombre(nombre) == False:
            return "El nombre no es valido."
        if validar_solicitud.validar_apellido(apellido) == False:
            return "El apellido no es valido."
        if validar_solicitud.validar_identificacion(identificacion) == False:
            return "La identificacion no es valido."        
        if validar_solicitud.validar_edad(edad) == False:
            return "La edad no es valida."
        if validar_solicitud.validar_afinidad_magia(afinidad_magia) == False:
            return "La afinidad_magia no es valido."
        return True

class validar_solicitud(object):
    def validar_nombre(nombre):
        if nombre.isalpha() and len(nombre)<=20 and nombre!="":        
            return True
        else:
            return False
    def validar_apellido(apellido):
        if apellido.isalpha() and len(apellido)<=20 and apellido!="":
            return True
        else:
            return False
    def validar_identificacion(identificacion):        
        if identificacion.isalnum() and len(identificacion)<=10 and identificacion!="":
            return True
        else:
            return False
    def validar_edad(edad):
        if str(edad).isdigit() and len(str(edad))<=2 and len(str(edad))>=1:
            return True
        else:
            return False
    def validar_afinidad_magia(afinidad_magia):
        if afinidad_magia == "":
            return False
        magia_A = ["Oscuridad",
        "Luz",
        "Fuego",
        "Agua",
        "Viento",
        "Tierra"]
        for item in magia_A:
            if item == str(afinidad_magia):
                return True
        return False
    """docstring for validar_solicitud_de_registro"""
    def __init__(self, arg):
        super(validar_solicitud_de_registro, self).__init__()
        self.arg = arg

class grimorios:
    def obtener_categoria(num_hojas):        
        if num_hojas == 1:
            return "Sinceridad"
        if num_hojas == 2:
            return "Esperanza"
        if num_hojas == 3:
            return "Amor"
        if num_hojas == 4:
            return "Buena fortuna"
        if num_hojas == 5:
            return "Desesperacion"
        return "NULL"
    def obtener_grimorio():
        trevol_hojas = [1, 2, 3, 4, 5]
        return random.choice(trevol_hojas)
# ------------------------------------------------------
def obj_covert_to_array(obj):
    array1 = []
    aux = []
    try:
        for item in obj:
            aux = [] # clean
            for item2 in item:                
                aux.append(item2)                
            array1.append(aux)
    except Exception as e:
        # print("ERROR en obj_covert_to_array(obj):") # DEBUG
        # print("ERROR:"+str(e)) # DEBUG
        pass
    return array1

class solicitudes:
    def get_total():
        conn = connection()
        # -----------------------------------------------
        text1 = "SELECT nombre,apellido,identificacion,edad,afinidad_magia,grimorio,estatus FROM  "+DataBase+".solicitudes;"
        # print(text1)    
        sql_text = text( text1 )
        result = conn.execute(sql_text)
        # -----------------------------------------------        
        conn.close()

        # result
        total = obj_covert_to_array(result)
        return total

    def eliminar_solicitud(nombre,identificacion):
        try:
            conn = connection()
            # -----------------------------------------------
            text1 = "DELETE FROM  "+DataBase+".solicitudes WHERE nombre = '"+nombre+"' and identificacion = '"+identificacion+"';"
            # print(text1)    
            sql_text = text( text1 )
            result = conn.execute(sql_text)
            # -----------------------------------------------        
            conn.close()
        except Exception as e:
            return False
        return True
    def actualizar_estatus_solicitud(identificacion,estatus):
        try:
            conn = connection()
            # -----------------------------------------------
            text1 = "UPDATE "+DataBase+".solicitudes SET estatus= "+str(estatus)+" WHERE identificacion = '"+str(identificacion)+"';"
            # print(text1)    
            sql_text = text( text1 )
            result = conn.execute(sql_text)
            # -----------------------------------------------        
            conn.close()
        except Exception as e:
            return False
        return True
    def actualizar_solicitud_registro(nombre,apellido,identificacion,edad,afinidad_magia):
        try:
            conn = connection()
            # -----------------------------------------------
            text1 = "UPDATE  "+DataBase+".solicitudes SET  nombre= '"+str(nombre)+"', apellido= '"+str(apellido)+"', edad= "+str(edad)+", afinidad_magia= '"+str(afinidad_magia)+"' WHERE identificacion = '"+str(identificacion)+"';"
            # print(text1)    
            sql_text = text( text1 )
            result = conn.execute(sql_text)
            # -----------------------------------------------
            conn.close()
        except Exception as e:
            return False
        return True
    def consultar_grimorio(identificacion):
        aux = "NULL"
        try:
            conn = connection()
            # -----------------------------------------------
            text1 = "SELECT grimorio FROM  "+DataBase+".solicitudes WHERE identificacion='"+identificacion+"' ;"        
            # print(text1)    
            sql_text = text( text1 )
            result = conn.execute(sql_text)
            # -----------------------------------------------
            conn.close()
            # result
            aux = obj_covert_to_array(result)
        except Exception as e:
            return False
        return aux

# ------------------------------------------------------
# API

@app.route('/API/hello', methods=['GET'])
def api_hello():    
    return '{mensaje: "Hola mundo API - Academia de magia"}'

# Enviar solicitud de ingreso/crear.
# Actualizar solicitud de ingreso.
# Actualizar estatus de solicitud.
# Consultar todas las solicitudes.
# Consultar asignaciones de Grimorios.
# Eliminar solicitud de ingreso.

@app.route('/API/crear_solicitud', methods=['POST'])
def crear_solicitud():    
    # ----------------------------------------------    
    dataj = json.loads(request.data)    
    # print(dataj["nombre"])
    # print(dataj["apellido"])
    nombre = dataj["nombre"]
    apellido = dataj["apellido"]
    identificacion = dataj["identificacion"]
    edad = dataj["edad"]
    afinidad_magia = dataj["afinidad_magia"]
    print(nombre)
    print(apellido)
    print(identificacion)
    print(edad)
    print(afinidad_magia)
    # --------------------------------------------------------
    # Validar datos
    resultado = VALIDAR.validar_datos(nombre,apellido,identificacion,edad,afinidad_magia)
    if resultado == True:
        # asignar grimorio
        grimorio = grimorios.obtener_grimorio()
        grimorio = grimorios.obtener_categoria(grimorio)
        print("grimorio:"+grimorio)
        # guardar registro
        aux = guardar.guardar_registro(nombre,apellido,identificacion,edad,afinidad_magia,grimorio)
        if aux == True:
            return '{ "titulo" : "Academia de magia", "mensaje":"Registro de solicitud exitoso", "grimorio":"'+grimorio+'" }'
            # 
        else:
            return '{ "titulo" : "Academia de magia", "mensaje":"Error al guardar, intetelo de nuevo.", "grimorio":"" }'
            #                 
    else:
        return '{ "titulo" : "Academia de magia", "mensaje":"SOLICITUD CANCELADA", "grimorio":"" }'
        #
    # ----------------------------------------------
    return "{crear_solicitud: 'Test'}"

@app.route('/API/actualizar_solicitud', methods=['POST'])
def api_actualizar_solicitud():
    # NOTA: la actulizacion se realiza por la "idntificacion"
    dataj = json.loads(request.data)

    identificacion = dataj["identificacion"]
    nombre = dataj["nombre"]
    apellido = dataj["apellido"]    
    edad = dataj["edad"]
    afinidad_magia = dataj["afinidad_magia"]

    print(identificacion)
    print(nombre)
    print(apellido)    
    print(edad)
    print(afinidad_magia)
    # --------------------------------------------------------
    resultado = VALIDAR.validar_datos(nombre,apellido,identificacion,edad,afinidad_magia)
    if resultado == True:        
        # actulizar registro
        aux = False
        aux = solicitudes.actualizar_solicitud_registro(nombre,apellido,identificacion,edad,afinidad_magia)
        if aux == True:
            return '{ "titulo" : "Academia de magia", "mensaje":"Actualizacion de registro de solicitud exitoso." }'
            # 
        if aux == False:
            return '{ "titulo" : "Academia de magia", "mensaje":"Error al actulizar la solicitud, intetelo de nuevo." }'
            #                 
    else:
        return '{ "titulo" : "Academia de magia", "mensaje":"Error al validar la actulizacion de la solicitud" }'
        #
    # --------------------------------------------------------        
    return '{"Actulizar_solicitud": "Test"}'

@app.route('/API/actualizar_estatus_solicitud', methods=['PUT'])
def api_actualizar_estatus_solicitud():
    dataj = json.loads(request.data)        
    identificacion = dataj["identificacion"]
    estatus = dataj["estatus"]
    print(identificacion)
    print(estatus)
    aux = solicitudes.actualizar_estatus_solicitud(identificacion,estatus)
    if aux == True:
        return '{ "titulo" : "Academia de magia", "mensaje":"EL ESTATUS DE LA SOLICITUD A SIDO ACTULIZADO" }'
    if aux == False:
        return '{ "titulo" : "Academia de magia", "mensaje":"Error al actualizar el estatus de la solicitud." }'    
    return "{Actualizar_estatus_solicitud: 'Test'}"

@app.route('/API/solicitudes', methods=['GET'])
def view_solicitudes():
    total = solicitudes.get_total()
    print(total)
    return "{solicitudes: "+str(total)+"}"
# ------
@app.route('/API/consultar_grimorio', methods=['POST'])
def consultar_grimorio():
    dataj = json.loads(request.data)        
    identificacion = dataj["identificacion"]       
    print(identificacion)
    aux = solicitudes.consultar_grimorio(identificacion)
    if aux != False:
        return '{ "titulo" : "Academia de magia", "mensaje":"CONSULTA DE GRIMORIO EXITOSO", "grimorio":"'+str(aux)+'" }'
    if aux == False:
        return '{ "titulo" : "Academia de magia", "mensaje":"Error al consultar grimorio, intentelo de nuevo." }'
    return "{consultar_grimorio: 'Test'}"

@app.route('/API/eliminar_solicitud', methods=['DELETE'])
def api_eliminar_solicitud():
    dataj = json.loads(request.data)    
    nombre = dataj["nombre"]    
    identificacion = dataj["identificacion"]
    print(nombre)    
    print(identificacion)
    aux = solicitudes.eliminar_solicitud(nombre,identificacion)
    if aux == True:
        return '{ "titulo" : "Academia de magia", "mensaje":"SOLICITUD ELIMINADA" }'
    if aux == False:
        return '{ "titulo" : "Academia de magia", "mensaje":"Error al eliminar solicitud, intentelo de nuevo." }'
    return "{eliminar_solicitud: 'Test'}"



    

# ------------------------------------------------------



if(__name__ == '__main__'):
    app.secret_key = "ThisIsNotASecret:p"
    db.create_all()
    # app.run()
    app.run(debug=True, port=5000, host='0.0.0.0')
    # app.run(debug=False, port=5000, host='0.0.0.0')
