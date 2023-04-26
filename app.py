from flask import Flask, url_for, render_template, request, redirect, session
from flask_sqlalchemy import SQLAlchemy

# CONFIG LOCAL
host = "localhost:3306"
user = "root"
password = "54321bd"
DataBase = 'bd_reino_del_trevol'

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://'+user+':'+password+'@'+host+'/'+DataBase
db = SQLAlchemy(app)

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

    #return "registrar_solicitud.html"
    # return render_template('registrar_solicitud.html')
    if request.method == 'GET':
        return render_template('login.html')
    else:
        if session.get('logged_in'):
            return render_template('registrar_solicitud.html')
        else:
            return render_template('index.html', message="Hello!")
        # return render_template('index.html', message="Incorrect Details")

# /registrar_solicitud_de_estudiante/
@app.route('/registrar_solicitud_de_estudiante/', methods=['GET','POST'])
def registrar_solicitud_de_estudiante():

    #return "registrar_solicitud.html"
    # return render_template('registrar_solicitud.html')
    if request.method == 'GET':
        return render_template('login.html')
    else:
        if session.get('logged_in'):
            # return render_template('registrar_solicitud.html')
            nombre = request.form['Nombre']
            apellido = request.form['Apellido']
            identificacion = request.form['Identificacion']
            edad = request.form['Edad']
            afinidad_magia = request.form['Afinidad_magia']
            print(nombre)
            print(apellido)
            print(identificacion)
            print(edad)
            print(afinidad_magia)
            # REALIZAR VALIDAION DEL FORM
            print("nombre es: " + str(validar_solicitud.validar_nombre(nombre) ) )
            print("Edad es: " + str(validar_solicitud.validar_edad(edad) ) )
            
            return "Realizar validacion de datos del formulario de registro de solicitud"
        else:
            return render_template('index.html', message="Hello!")
        # return render_template('index.html', message="Incorrect Details")
# ------------------------------------------------------
class validar_solicitud(object):

    def validar_nombre(nombre):
        if nombre.isalpha() and len(nombre)<=20 and nombre!="":        
            return True
        else:
            return False
    def validar_apellido(apellido):
        if "N" in str(apellido):
            return True
        else:
            return False
    def validar_identificacion(identificacion):
        if "N" in str(identificacion):
            return True
        else:
            return False
    def validar_edad(edad):
        if str(edad).isdigit() and len(str(edad))<=2:
            return True
        else:
            return False
    def validar_afinidad_magia(afinidad_magia):
        if "N" in str(afinidad_magia):
            return True
        else:
            return False


    """docstring for validar_solicitud_de_registro"""
    def __init__(self, arg):
        super(validar_solicitud_de_registro, self).__init__()
        self.arg = arg


        

# ------------------------------------------------------
# API

@app.route('/API/hello', methods=['GET'])
def api_hello():    
    return '{mensaje: "Hola mundo API"}'

# ------------------------------------------------------



if(__name__ == '__main__'):
    app.secret_key = "ThisIsNotASecret:p"
    db.create_all()
    # app.run()
    app.run(debug=True, port=5000, host='0.0.0.0')
    # app.run(debug=False, port=5000, host='0.0.0.0')
