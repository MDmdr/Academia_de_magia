# Academia de magia

Aplicacion Flask para manejar el registro de solicitudes de estudiantes en la academia de magia.
  
Configuracion y despliegue:
En la linea de comandos:

git clone https://github.com/MDmdr/Academia_de_magia.git
cd Academia_de_magia

# Configurar la base de datos
Crear una nueva base de datos en su sistema gestor nombre: "academia_de_magia".
Import la base de datos contenida en al archivo "/Academia_de_magia/academia_de_magia.sql".
cofigurar el acceso de la aplicacion a la base de datos en los archivos:
"/Academia_de_magia/app.py"
"/Academia_de_magia/queries_DB/connectionDB.py"
"/Academia_de_magia/cargar_tipos_de_magia/cargar_datos.py"
nota: cargar_datos.py sirve para cargar los datos del archivo csv, pero si importo la base, estos ya estaria cargados, y no sera nesesario ejecutarlo de nuevo.
Configurar accesos sobre las variables:
host = "".
user = "".
password = "".
DataBase = ''.

# Instalar los requerimientos
cd Academia_de_magia
pip install -r requirements.txt
# Desplegar la aplicación:
python app.py

Para abrir la aplicacion colocar "http://localhost:5000/" en el navegador.
Para navegar y usar la aplicacion web.,


# API por postman ejemplos
# crear solicitud, ejemplo:
Metodo: POST
http://localhost:5000/API/crear_solicitud
{
"nombre" : "JoseMaria",
"apellido" : "Martinez",
"identificacion" : "Identi002",
"edad" : "15",
"afinidad_magia" : "Luz"
}

# Eliminar solicitud
Metodo: DELETE
http://localhost:5000/API/eliminar_solicitud
{
"nombre" : "mdrNewg",
"identificacion" : "10005"
}

# Actulizar el registro de la solicitud a partir de su "idetificacion":
Metodo: POST
http://localhost:5000/API/actualizar_solicitud
{
"identificacion": 10005,
"nombre": "Miguel",
"apellido": "Hidalgo",    
"edad": "55",
"afinidad_magia": "Fuego"
}

# Actulizar el estatus de la solicitud
Metodo: PUT
http://localhost:5000/API/actualizar_estatus_solicitud
{
"identificacion" : "10005",
"estatus" : "2"
}

# Consultar grimorio apartir de la idetificacion
Metodeo: POST
http://localhost:5000/API/consultar_grimorio
{
"identificacion" : "10005"
}

# Ver todas la solicitudes registradas
Metodo: GET
http://localhost:5000/API/solicitudes