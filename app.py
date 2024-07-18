import streamlit as st
import numpy as np
import pickle
import pandas as pd

# Título de la aplicación
st.title('Predicción del Ganador de la Partida en CS:GO')

# Cargar el modelo y los label encoders desde los archivos .pkl
model_filename = 'logistic_regression_model.pkl'
label_encoder_map_filename = 'label_encoder_map.pkl'
label_encoder_team_filename = 'label_encoder_team.pkl'

with open(model_filename, 'rb') as file:
    model = pickle.load(file)

with open(label_encoder_map_filename, 'rb') as file:
    label_encoder_map = pickle.load(file)

with open(label_encoder_team_filename, 'rb') as file:
    label_encoder_team = pickle.load(file)

# Inputs del usuario
mapa = st.selectbox('Selecciona el Mapa', label_encoder_map.classes_)
equipo = st.selectbox('Selecciona el Equipo', label_encoder_team.classes_)
headshots = st.number_input('Ingresa el número estimado de MatchHeadshots', min_value=0)

# Función para hacer la predicción
def hacer_prediccion():
    # Convertir los inputs a formato adecuado para el modelo
    mapa_encoded = label_encoder_map.transform([mapa])[0]
    equipo_encoded = label_encoder_team.transform([equipo])[0]

    # Crear un DataFrame con los nombres de las características
    input_data = np.array([[mapa_encoded, equipo_encoded, headshots]])
    input_df = pd.DataFrame(input_data, columns=['Map', 'Team', 'MatchHeadshots'])

    # Hacer la predicción y obtener la probabilidad
    probabilidad = model.predict_proba(input_df)[0]
    # Clase 1 es la probabilidad de que el equipo gane
    probabilidad_ganar = probabilidad[1] * 100

    # Mostrar el resultado con la probabilidad
    if probabilidad_ganar > 50:
        st.success(f'Es probable que el equipo haya ganado la partida con una probabilidad del {probabilidad_ganar:.2f}%.')
    else:
        st.error(f'Es probable que el equipo haya perdido la partida con una probabilidad del {(100 - probabilidad_ganar):.2f}%.')

# Botón para hacer la predicción
if st.button('Hacer Predicción'):
    hacer_prediccion()
