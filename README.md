# Índice

1. [Descripción del Proyecto](#vende-fácil)
2. [Tecnologías Utilizadas](#tecnologías-utilizadas)
   - [Backend](#backend)
   - [Frontend](#frontend)
   - [Herramientas de Desarrollo](#herramientas-de-desarrollo)
3. [Sistema Operativo](#sistema-operativo)
4. [Comandos de Instalación](#comandos-de-instalación)
   - [Instalación de Python](#instalación-de-python)
   - [Instalación de Virtualenv](#instalación-de-virtualenv)
   - [Verificar si el entorno virtual está activo](#verificar-si-el-entorno-virtual-está-activo)
   - [Instalación de Flask y Herramientas Adicionales](#instalación-de-flask-y-herramientas-adicionales)
5. [Inicializar el Proyecto](#inicializar-el-proyecto)
   - [Verificar si el servidor está corriendo](#verificar-si-el-servidor-está-corriendo)
6. [Solución a Errores Comunes](#solución-a-errores-comunes)
7. [Metodología de Trabajo](#metodología-de-trabajo)
8. [Versión del Proyecto](#versión-del-proyecto)
9. [Autor e Institución](#autor-e-institución)
10. [Licencia](#licencia)

---

# Vende-Fácil

Vende-Fácil es una aplicación desarrollada para facilitar la conexión entre vendedores de productos agrícolas y compradores de alimentos del campo. Su propósito principal es actuar como intermediaria digital, permitiendo la gestión eficiente de ventas, compras, productos y usuarios dentro del ecosistema agrícola.

La plataforma maneja distintos tipos de usuarios (clientes y vendedores), así como el registro de productos con sus características específicas (tipo, tamaño, precio, disponibilidad). También permite realizar ventas y compras, y relacionarlas con los productos comercializados.

---

## Tecnologías Utilizadas

### Backend
- Python
- JSON
- Flask
- Postman
- PostgreSQL
- Jinja2
- ENV o VENV

### Frontend
- HTML
- CSS
- JavaScript
- Framework Bootstrap

### Herramientas de Desarrollo
- Git
- GitHub
- Visual Studio Code
- Copilot Pro
- Canva
- Creadores de UML

---

## Sistema Operativo
- Windows 11

---

## Comandos de Instalación

### Instalación de Python
1. Descarga Python desde su [sitio oficial](https://www.python.org/downloads/).
2. Durante la instalación, asegúrate de marcar la opción **"Add Python to PATH"**.
3. Verifica la instalación ejecutando:
   ```
   python --version
   ```
   o
   ```
   python3 --version
   ```

### Instalación de Virtualenv
1. Instala `virtualenv` utilizando `pip`:
   ```
   pip install virtualenv
   ```

2. Crea un entorno virtual con Python 3:
   ```
   virtualenv -p python3 env
   ```

3. Activa el entorno virtual:
   - En Windows (Git Bash desde Visual Studio Code):
     ```
     source env/Scripts/activate
     ```
   - En Windows (Command Prompt o PowerShell):
     ```
     .\env\Scripts\activate
     ```
   - En Linux/Mac:
     ```
     source env/bin/activate
     ```

### Verificar si el entorno virtual está activo

Para verificar si el entorno virtual está activo sin intentar activarlo nuevamente, puedes usar el siguiente comando:

- En Git Bash o cualquier terminal compatible con Bash:
  ```bash
  echo $VIRTUAL_ENV
  ```
  Si el entorno virtual está activo, este comando mostrará la ruta al entorno virtual (por ejemplo, `p:/GITHUB/PROYECTOS/VENDEFACIL/env`). Si no está activo, no mostrará nada o estará vacío.

- En PowerShell:
  ```powershell
  $env:VIRTUAL_ENV
  ```
  Esto también mostrará la ruta al entorno virtual si está activo. Si no está activo, no mostrará nada.

### Ruta a seguir si no está activo

1. Si el entorno virtual no está activo, actívalo con el comando correspondiente:
   - En Git Bash:
     ```bash
     source env/Scripts/activate
     ```
   - En PowerShell:
     ```powershell
     .\env\Scripts\activate
     ```
   - En Command Prompt (CMD):
     ```cmd
     .\env\Scripts\activate.bat
     ```

2. Una vez activado, verifica nuevamente con el comando `echo $VIRTUAL_ENV` o `$env:VIRTUAL_ENV` según el terminal que estés utilizando.

### Instalación de Flask y Herramientas Adicionales

Para instalar Flask y otras herramientas necesarias, utiliza los siguientes comandos:

1. Instalar Flask:
   ```bash
   pip install flask
   ```

2. Instalar setuptools:
   ```bash
   pip install setuptools
   ```

3. Instalar wheel:
   ```bash
   pip install wheel
   ```

Asegúrate de que estás dentro del entorno virtual antes de ejecutar estos comandos. Puedes verificarlo con el comando `echo $VIRTUAL_ENV` o `$env:VIRTUAL_ENV` según el terminal que estés utilizando.

---

### Inicializar el Proyecto

Para inicializar el proyecto, asegúrate de estar en la ruta de la carpeta `app` y ejecuta el siguiente comando:

```bash
py ./app/app.py
```

Este comando iniciará el servidor Flask y pondrá en marcha la aplicación.

### Verificar si el servidor está corriendo

Después de inicializar el proyecto, puedes abrir tu navegador y visitar el siguiente enlace para verificar si el servidor Flask está funcionando correctamente:

[http://127.0.0.1:5000](http://127.0.0.1:5000)

Si el servidor está corriendo, deberías ver la página de inicio o la respuesta configurada en tu aplicación Flask.

---

## Solución a Errores Comunes

Si encuentras problemas al ejecutar el proyecto, sigue estos pasos para solucionarlos:

1. **Verificar las rutas**:
   - Asegúrate de que las rutas en el navegador sean correctas.
   - Por ejemplo, para acceder a la página principal, utiliza: `http://127.0.0.1:5000/`.

2. **Cerrar y abrir Visual Studio Code**:
   - Si los cambios en el código no se reflejan, intenta cerrar y volver a abrir Visual Studio Code.

3. **Actualizar la página web**:
   - Presiona `Ctrl + F5` en el navegador para forzar la recarga de la página y evitar el uso de caché.

4. **Reiniciar el servidor local**:
   - Detén el servidor Flask y vuelve a iniciarlo con el comando:
     ```
     py ./app/app.py
     ```

5. **Cerrar y abrir una nueva terminal**:
   - Si el entorno virtual o los comandos no funcionan correctamente, cierra la terminal actual y abre una nueva.
   - Asegúrate de activar el entorno virtual nuevamente antes de ejecutar comandos.

---

## Metodología de Trabajo

Este proyecto utiliza la metodología **Kanban** para la gestión y organización de tareas. Kanban permite visualizar el flujo de trabajo, identificar cuellos de botella y mejorar la eficiencia del equipo.

---

## Versión del Proyecto

Este proyecto está actualmente en la versión **0.0.1**, lo que indica que se encuentra en una etapa muy temprana de desarrollo. A medida que se implementen más funcionalidades y se realicen mejoras, la versión será actualizada siguiendo el esquema de versionado semántico.

---

## Autor e Institución
**Autor:** Milton Figueredo  
[LinkedIn](https://www.linkedin.com/in/milton-figueredo-miles-arts/)  
[GitHub](https://github.com/Miles-Arts)  
**Institución:** SENA - Servicio Nacional de Aprendizaje  
**Programa:** Tecnólogo en Análisis y Desarrollo de Software  
**Fecha:** Mayo 2025

---

# Licencia

Este proyecto está licenciado bajo la Licencia MIT. Puedes ver el archivo de licencia completo a continuación:

```
MIT License

Copyright (c) 2025 Milton Figueredo

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

---
