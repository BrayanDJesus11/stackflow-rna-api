import pandas as pd
import random

data = []

for i in range(5000):

    edad = random.randint(18, 70)

    frecuencia_compra = random.randint(1, 20)

    monto_promedio = random.randint(5000, 500000)

    dias_ultima_compra = random.randint(1, 180)

    satisfaccion = round(
        random.uniform(1, 5),
        1
    )

    total_historico = (
        frecuencia_compra
        * monto_promedio
    )

    cantidad_productos = random.randint(1, 15)

    usa_tarjeta = random.randint(0, 1)


    score = 0

    if frecuencia_compra > 5:
        score += 1

    if dias_ultima_compra < 30:
        score += 1

    if satisfaccion >= 4:
        score += 1

    if total_historico > 300000:
        score += 1

    if usa_tarjeta == 1:
        score += 1

    recompra = 1 if score >= 3 else 0

    data.append([

        edad,

        frecuencia_compra,

        monto_promedio,

        dias_ultima_compra,

        satisfaccion,

        total_historico,

        cantidad_productos,

        usa_tarjeta,

        recompra
    ])

columns = [

    "edad",

    "frecuenciaCompra",

    "montoPromedio",

    "diasUltimaCompra",

    "satisfaccion",

    "totalHistorico",

    "cantidadProductos",

    "usaTarjeta",

    "recompra"
]

df = pd.DataFrame(
    data,
    columns=columns
)

df.to_csv(
    "dataset_recompras.csv",
    index=False
)

print(
    "Dataset generado correctamente"
)