import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Título da página
st.title("Dashboard Interativo com Streamlit")

# Adicionando uma descrição
st.write("""
Esta aplicação permite visualizar um gráfico interativo gerado a partir de dados aleatórios.
Você pode ajustar os parâmetros e ver como o gráfico muda em tempo real.
""")

# Seleção de dados
data_size = st.slider("Escolha o número de pontos de dados:", 10, 100, 50)
data_type = st.selectbox("Escolha o tipo de dado:", ["Aleatório", "Seno", "Cosseno"])

# Gerar dados
if data_type == "Aleatório":
    data = np.random.randn(data_size)
elif data_type == "Seno":
    data = np.sin(np.linspace(0, 2 * np.pi, data_size))
else:
    data = np.cos(np.linspace(0, 2 * np.pi, data_size))

# Exibir os dados em uma tabela
st.write("Dados gerados:")
st.write(pd.DataFrame(data, columns=["Valor"]))

# Plotar o gráfico
plt.figure(figsize=(10, 5))
plt.plot(data, marker='o')
plt.title(f"Gráfico de Dados ({data_type})")
plt.xlabel("Índice")
plt.ylabel("Valor")
st.pyplot(plt)

# Adicionar uma seção para feedback
st.write("Por favor, compartilhe suas opiniões:")
feedback = st.text_area("Seu feedback:")
if st.button("Enviar"):
    st.write("Obrigado pelo seu feedback!")

