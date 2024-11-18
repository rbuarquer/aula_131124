import streamlit as st
import pandas as pd
import requests

# Fetch data from the URLs using requests
url_mulheres = 'https://dadosabertos.camara.leg.br/api/v2/deputados?siglaSexo=F&ordem=ASC&ordenarPor=nome'
response_mulheres = requests.get(url_mulheres)
data_mulheres = response_mulheres.json()['dados'] #Extract data from JSON response

url_homens = 'https://dadosabertos.camara.leg.br/api/v2/deputados?siglaSexo=M&ordem=ASC&ordenarPor=nome'
response_homens = requests.get(url_homens)
data_homens = response_homens.json()['dados'] #Extract data from JSON response

# Create DataFrames from the fetched data
dfmulheres = pd.DataFrame(data_mulheres)
dfmulheres['sexo'] = 'F'
dfhomens = pd.DataFrame(data_homens)
dfhomens['sexo'] = 'M'
df = pd.concat([dfmulheres, dfhomens])


# Título do dashboard
st.title("Dashboard de Parlamentares")

# Selectbox para escolher o gênero
genero = st.selectbox(
    "Selecione o gênero para filtrar:",
    options=["Todos", "Feminino", "Masculino"]
)

# Filtragem por gênero
if genero == "Feminino":
    df_filtrado = df[df['sexo'] == 'F']
elif genero == "Masculino":
    df_filtrado = df[df['sexo'] == 'M']
else:
    df_filtrado = df

# Exibindo os dados filtrados
st.dataframe(df_filtrado)

# Exibindo contagem por gênero
st.write("Contagem por gênero:")
st.write(df['sexo'].value_counts())

