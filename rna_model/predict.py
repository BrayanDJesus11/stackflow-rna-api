import sys
import json
import joblib
import numpy as np

from tensorflow.keras.models import load_model


model = load_model(
    "modelo_recompra.h5"
)

scaler = joblib.load(
    "scaler.pkl"
)


input_data = {

    "edad": 25,

    "frecuenciaCompra": 10,

    "montoPromedio": 50000,

    "diasUltimaCompra": 5,

    "satisfaccion": 4.8,

    "totalHistorico": 400000,

    "cantidadProductos": 5,

    "usaTarjeta": 1
}


data = [[

    input_data["edad"],

    input_data["frecuenciaCompra"],

    input_data["montoPromedio"],

    input_data["diasUltimaCompra"],

    input_data["satisfaccion"],

    input_data["totalHistorico"],

    input_data["cantidadProductos"],

    input_data["usaTarjeta"]
]]


data_scaled = scaler.transform(data)

prediction = model.predict(
    data_scaled
)

probabilidad = float(
    prediction[0][0]
)

resultado = (

    "SI"

    if probabilidad >= 0.5

    else "NO"
)


response = {

    "resultado": resultado,

    "probabilidad": round(
        probabilidad * 100,
        2
    )
}

print(
    json.dumps(response)
)