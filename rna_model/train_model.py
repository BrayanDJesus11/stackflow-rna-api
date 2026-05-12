import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

import joblib


df = pd.read_csv(
    "dataset_recompras.csv"
)


X = df.drop(
    "recompra",
    axis=1
)

y = df["recompra"]


scaler = StandardScaler()

X_scaled = scaler.fit_transform(X)

# Guardar scaler
joblib.dump(
    scaler,
    "scaler.pkl"
)

X_train, X_test, y_train, y_test = train_test_split(

    X_scaled,

    y,

    test_size=0.2,

    random_state=42
)

model = Sequential()

model.add(
    Dense(
        16,
        activation="relu",
        input_shape=(X_train.shape[1],)
    )
)

model.add(
    Dense(
        8,
        activation="relu"
    )
)

model.add(
    Dense(
        1,
        activation="sigmoid"
    )
)

model.compile(

    optimizer="adam",

    loss="binary_crossentropy",

    metrics=["accuracy"]
)

model.fit(

    X_train,

    y_train,

    epochs=40,

    batch_size=32,

    validation_split=0.2
)


loss, accuracy = model.evaluate(
    X_test,
    y_test
)

print(
    f"\nPrecisión del modelo: {accuracy * 100:.2f}%"
)


model.save(
    "modelo_recompra.h5"
)

print(
    "\nModelo guardado correctamente 😎🔥"
)