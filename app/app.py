from flask import Flask 
from flask import render_template

# Crear una instancia de la aplicación Flask
app=Flask(__name__)

# Definir la ruta principal de la aplicación
@app.route('/')
def index():
    # Crear una lista de cursos
    cursos=["PHP", "Python", "Java", "Go", "Cobol", "C++"]
    # Crear un diccionario con datos para pasar a la plantilla
    data={
        'titulo': 'Inicio',
        'bienvenida': 'Holaaa',
        "cursos": cursos,
        "numero_cursos": len(cursos)
    }
    # Renderizar la plantilla HTML 'index.html' para la página principal
    return render_template('index.html', data=data)

@app.route('/contacto/<nombre>/<int:edad>')
def contacto(nombre, edad):
    # Crear un diccionario con datos para pasar a la plantilla
    data={
        'titulo': 'Contacto',
        'nombre': nombre,
        'edad': edad
    }
    # Renderizar la plantilla HTML 'contacto.html' para la página de contacto
    return render_template('contacto.html', data=data)

# Verificar si el archivo se está ejecutando directamente
if __name__=="__main__":
    # Ejecutar la aplicación Flask en modo de depuración y en el puerto 5000
    app.run(debug=True, port=5000)
