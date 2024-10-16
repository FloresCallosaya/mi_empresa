from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/quienes")
def quienes():
    return render_template("quienes.html")

@app.route("/servicios")
def servicios():
    return render_template("servicios.html")

@app.route("/noticias")
def noticias():
    return render_template("noticias.html")

@app.route("/contacto", methods=['GET'])
def contacto():
    return render_template("contacto.html")

# Ruta para procesar el formulario de contacto
@app.route("/enviar_contacto", methods=['POST'])
def enviar_contacto():
    nombre = request.form.get('nombre')
    correo = request.form.get('correo')
    mensaje = request.form.get('mensaje')

    # Aquí puedes procesar los datos del formulario (ej. guardarlos o enviarlos por email)
    print(f"Nombre: {nombre}, Correo: {correo}, Mensaje: {mensaje}")

    return redirect(url_for('contacto'))  # Redirige de nuevo a la página de contacto tras el envío

if __name__ == "__main__":
    app.run(debug=True)
