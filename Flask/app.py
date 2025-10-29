#Martinez Lamadrid Santiago Ivan
#4A
#29/10/2025
from flask import Flask, request, render_template_string

app = Flask(__name__)

@app.route('/formulario', methods=['GET', 'POST'])
def formulario():
    resultado = None
    nombre = None

    if request.method == 'POST':
        try:
            # Obtener los datos del formulario
            a = float(request.form['a'])
            b = float(request.form['b'])
            c = float(request.form['c'])
            nombre = request.form['nombre']

            # Calcular el resultado
            resultado = (a + b) / c
        except Exception as e:
            resultado = f"Error: {str(e)}"

    # Plantilla HTML embebida
    html = """
    <html>
    <head>
        <title>Formulario Flask</title>
        <style>
            body { font-family: Arial; margin: 40px; background: #f0f0f0; }
            form { background: white; padding: 20px; border-radius: 10px; width: 300px; }
            input { margin-bottom: 10px; width: 100%; padding: 8px; }
            button { background-color: green; color: white; padding: 10px; border: none; cursor: pointer; width: 100%; }
            .resultado { margin-top: 20px; background: #dff0d8; padding: 15px; border-radius: 8px; font-size: 18px; }
        </style>
    </head>
    <body>
        <h2>Formulario de Suma y División</h2>
        <form method="POST">
            <input type="text" name="nombre" placeholder="Tu nombre" required><br>
            <input type="number" name="a" step="any" placeholder="Número A" required><br>
            <input type="number" name="b" step="any" placeholder="Número B" required><br>
            <input type="number" name="c" step="any" placeholder="Número C" required><br>
            <button type="submit">Calcular</button>
        </form>

        {% if resultado is not none %}
            <div class="resultado">
                <strong>Hola {{ nombre }}!</strong><br>
                El resultado de (A + B) / C es: <b>{{ resultado }}</b>
            </div>
        {% endif %}
    </body>
    </html>
    """

    return render_template_string(html, resultado=resultado, nombre=nombre)

if __name__ == '__main__':
    app.run(debug=True)
