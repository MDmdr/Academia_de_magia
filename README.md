# Academia de magia

Aplicacion Flask para manejar el registro de solicitudes de estudiantes en la academia de magia.
  
Configuracion y despliegue:

git clone https://github.com/MDmdr/Academia_de_magia.git
cd Academia_de_magia
? virtualenv venv -p python3
? source venv/bin/activate
pip install -r requirements.txt
python app.py


Para abrir la aplicacion colocar "http://localhost:5000/" en el navegador.


# API por postman
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

# -------------------
