import streamlit as st

# Título de la aplicación
st.title("Ejemplo Sencillo en Streamlit")

# Texto inicial
st.write("¡Bienvenido a mi aplicación en Streamlit!")

# Botón para cambiar el saludo
if st.button("Cambiar mensaje"):
    st.write("¡Has presionado el botón! Bienvenido de nuevo.")
else:
    st.write("Presiona el botón para cambiar el mensaje.")
