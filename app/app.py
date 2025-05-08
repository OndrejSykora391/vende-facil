from flask import Flask 
from flask import render_template

app=Flask(__name__)

@app.route('/')
def index():
    # return "<h1>Hola mi gente 😁</h1>"
    cursos=["PHP", "Python", "Java", "Go", "Cobol", "C++"]
    data={
        'titulo': 'index.html',
        'bienvenida': 'Holaaa',
        "cursos": cursos,
        "numero_cursos": len(cursos)
    }
    return render_template('index.html', data=data)

if __name__=="__main__":
    app.run(debug=True, port=5000)
