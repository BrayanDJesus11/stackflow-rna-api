from flask import Flask
from flask import request
from flask import jsonify

import joblib
import numpy as np

from tensorflow.keras.models import load_model

app = Flask(__name__)

print("Cargando modelo RNA...")

model = load_model(
    "modelo_recompra.h5"
)

scaler = joblib.load(
    "scaler.pkl"
)

print("Modelo cargado correctamente")


@app.route("/")
def home():

    return "StackFlow RNA API funcionando"


@app.route(
    "/predict",
    methods=["POST"]
)

def predict():

    data = request.json

    values = [[

        data["edad"],

        data["frecuenciaCompra"],

        data["montoPromedio"],

        data["diasUltimaCompra"],

        data["satisfaccion"],

        data["totalHistorico"],

        data["cantidadProductos"],

        data["usaTarjeta"]
    ]]

    values_scaled = scaler.transform(
        values
    )

    prediction = model.predict(
        values_scaled
    )

    probabilidad = float(
        prediction[0][0]
    )

    resultado = (

        "SI"

        if probabilidad >= 0.5

        else "NO"
    )

    return jsonify({

        "resultado": resultado,

        "probabilidad": round(
            probabilidad * 100,
            2
        )
    })


if __name__ == "__main__":

    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )
