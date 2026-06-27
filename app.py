import streamlit as st

st.title("Aplicación de Fundamentos Stremlit")

st.sidebar.image("LogoUHE.png")

st.sidebar.title("Parámetros")

monto = st.number_input("Ingrese el monto de su préstamo")

interes = st.number_input("Ingrese el interes", value = 0.05)

tiempo_meses = st.number_input("Ingrese el tiempo en meses")

resultado = monto*interes+(tiempo_meses/12)


