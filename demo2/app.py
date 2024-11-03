import streamlit as st
import pandas as pd

# Título de la aplicación
st.title("Ejemplo Sencillo en Streamlit")

# Texto inicial
st.write("¡Bienvenido a mi aplicación en Streamlit!")

# Cargar el archivo CSV (debes tener el archivo titanic.csv en el mismo directorio o especificar la ruta correcta)
try:
    df = pd.read_csv("demo2/titanic.csv")
    st.write("Datos del Titanic:")
    st.dataframe(df)  # Mostrar el DataFrame en Streamlit
except FileNotFoundError:
    st.error("El archivo titanic.csv no se encontró. Asegúrate de que el archivo está en el directorio correcto.")

# Botón para cambiar el saludo
if st.button("Cambiar mensaje"):
    st.write("¡Has presionado el botón! Bienvenido de nuevo.")
else:
    st.write("Presiona el botón para cambiar el mensaje.")
