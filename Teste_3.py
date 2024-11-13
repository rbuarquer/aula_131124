import streamlit as st
st.title("Avaliação de Satisfação do Cliente")
st.write("Selecione o grau de satisfação do cliente na escala de 0 a 100.")
satisfacao = st.select_slider('Grau de Satisfação', options=range(101),  value=50)
st.write(f"Satisfação do cliente: {satisfacao}/100")
