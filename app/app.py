# Importar las bibliotecas necesarias de Flask
# Flask: Framework principal
# render_template: Para renderizar plantillas HTML
# request: Para manejar solicitudes HTTP
# url_for, redirect: Para redirecciones y generación de URLs dinámicas
from flask import Flask 
from flask import render_template
from flask import request
from flask import url_for, redirect


# Import routes
#from app import routes

# Crear la conexión a la base de datos
#conn = psycopg2.connect(
    #dbname="VendeFacil",
    #user="root",
    #password="1234",
   # host="localhost",
   # port="5432"
#)

# Crear un cursor para ejecutar consultas
#cursor = conn.cursor()

# Crear una instancia de la aplicación Flask
app=Flask(__name__)


# Middleware que se ejecuta antes de cada solicitud
@app.before_request
def before_request():
    # Imprime un mensaje antes de procesar la solicitud
    print("Antes de la petición...")

# Middleware que se ejecuta después de cada solicitud
@app.after_request
def after_request(response):
    # Imprime un mensaje después de procesar la solicitud
    print("Despues de la petición...")
    # Devuelve la respuesta al cliente
    return response

# Ruta principal de la aplicación
@app.route('/')
def index():
    # Lista de cursos disponibles
    cursos=["PHP", "Python", "Java", "Go", "Cobol", "C++"]
    # Diccionario con datos para pasar a la plantilla HTML
    data={
        'titulo': 'Inicio',
        'bienvenida': 'Holaaa',
        "cursos": cursos,
        "numero_cursos": len(cursos)
    }
    # Renderiza la plantilla 'index.html' con los datos proporcionados
    return render_template('index.html', data=data)

# Ruta para la página de contacto con parámetros dinámicos
@app.route('/contacto/<nombre>/<int:edad>')
def contacto(nombre, edad):
    # Diccionario con datos para pasar a la plantilla HTML
    data={
        'titulo': 'Contacto',
        'nombre': nombre,
        'edad': edad
    }
    # Renderiza la plantilla 'contacto.html' con los datos proporcionados
    return render_template('contacto.html', data=data)

# Ruta para manejar parámetros de consulta (query string)
def query_string():
    # Imprime la solicitud completa
    print(request)
    # Imprime los parámetros de consulta
    print(request.args)
    # Obtiene y muestra el valor del parámetro 'param1'
    print(request.args.get('param1'))
    # Obtiene y muestra el valor del parámetro 'param2'
    print(request.args.get('param2'))
    # Devuelve una respuesta simple
    return 'ok'

# Manejo de errores 404 (página no encontrada)
def pagina_no_encontrada(error):
    # Redirige al índice en caso de error 404
    return redirect(url_for('index'))

# Punto de entrada principal de la aplicación
if __name__=="__main__":
    # Agrega la ruta para manejar parámetros de consulta
    app.add_url_rule('/query_string', view_func=query_string)
    # Registra el manejador de errores 404
    app.register_error_handler(404,pagina_no_encontrada)
    # Ejecuta la aplicación Flask en modo de depuración y en el puerto 5000
    app.run(debug=True, port=5000)
