import streamlit as st
import pandas as pd
import scipy

st.title("Mi primera app con Streamlit")

st.write("Hola, mundo!")

# Ejemplo con pandas
df = pd.DataFrame({
    'Columna 1': [1, 2, 3],
    'Columna 2': [4, 5, 6]
})

st.write(df)