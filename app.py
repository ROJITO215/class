from flask import Flask
from controller import ciclista
from controlle import maillot  # Import the Blueprint
from cont import puerto
from contro import etapa

app = Flask(__name__)

app.register_blueprint(ciclista) # REGISTRAR LA RUTA QUE CREO EN EL CONTROLLER
app.register_blueprint(maillot)
app.register_blueprint(puerto)
app.register_blueprint(etapa)


if __name__ == '__main__':
    app.run(debug=True)
