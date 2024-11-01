import streamlit as st
import pandas as pd

# Configuração do título e das páginas
st.title("Cálculo de Margens Comerciais")
st.sidebar.title("Selecione a Página")
page = st.sidebar.selectbox("Escolha a margem:", ["Margem Absoluta", "Margem Relativa"])

# Função para exibir os cálculos das margens
def calculo_margens_absolutas(pv, pa, pp):
    margem_total = pv - pp
    margem_atacado = pa - pp
    margem_varejo = pv - pa
    st.write(f"Margem Total: {margem_total:.2f}")
    st.write(f"Margem do Atacado: {margem_atacado:.2f}")
    st.write(f"Margem do Varejo: {margem_varejo:.2f}")

def calculo_margens_relativas(preco_do_varejo, preco_do_atacado, preco_do_produtor):
    margem_total = (preco_do_varejo - preco_do_produtor) / preco_do_varejo * 100
    margem_varejo = (preco_do_varejo - preco_do_atacado) / preco_do_varejo * 100
    margem_atacado = (preco_do_atacado - preco_do_produtor) / preco_do_varejo * 100
    margem_produtor = (preco_do_produtor / preco_do_varejo) * 100
    st.write(f"Margem do Varejo: {margem_varejo:.2f}%")
    st.write(f"Margem do Atacado: {margem_atacado:.2f}%")
    st.write(f"Margem do Produtor: {margem_produtor:.2f}%")
    st.write(f"Margem Total: {margem_total:.2f}%")

# Se o usuário fizer o upload de um arquivo
uploaded_file = st.file_uploader("Escolha um arquivo", type=["xlsx", "csv"])
if uploaded_file:
    # Leitura do arquivo e exibição dos dados
    try:
        if uploaded_file.name.endswith('.csv'):
            data = pd.read_csv(uploaded_file)
        elif uploaded_file.name.endswith('.xlsx'):
            data = pd.read_excel(uploaded_file)

        st.write("Dados do arquivo carregado:")
        st.write(data)

        # Verificação se as colunas necessárias estão presentes no arquivo
        required_columns = ['Varejo', 'Atacado', 'Produtor']
        if all(col in data.columns for col in required_columns):
            for index, row in data.iterrows():
                pv, pa, pp = row['Varejo'], row['Atacado'], row['Produtor']
                st.write(f"## Linha {index + 1}")
                
                if page == "Margem Absoluta":
                    calculo_margens_absolutas(pv, pa, pp)
                elif page == "Margem Relativa":
                    calculo_margens_relativas(pv, pa, pp)
        else:
            st.error(f"Certifique-se de que o arquivo contém as colunas: {', '.join(required_columns)}")
    except Exception as e:
        st.error(f"Ocorreu um erro ao processar o arquivo: {e}")

# Interface manual para inserção de dados caso não tenha um arquivo
if not uploaded_file:
    if page == "Margem Absoluta":
        st.header("Cálculo da Margem Absoluta")
        pv = st.number_input('Informe o preço do Varejo:', min_value=0.0, format="%.2f")
        pa = st.number_input('Informe o preço do Atacado:', min_value=0.0, format="%.2f")
        pp = st.number_input('Informe o preço do Produtor:', min_value=0.0, format="%.2f")
        if st.button("Calcular"):
            calculo_margens_absolutas(pv, pa, pp)
    elif page == "Margem Relativa":
        st.header("Cálculo da Margem Relativa")
        preco_do_varejo = st.number_input('Informe o preço do varejo:', min_value=0.0, format="%.2f")
        preco_do_atacado = st.number_input('Informe o preço do atacado:', min_value=0.0, format="%.2f")
        preco_do_produtor = st.number_input('Informe o preço do produtor:', min_value=0.0, format="%.2f")
        if st.button("Calcular"):
            calculo_margens_relativas(preco_do_varejo, preco_do_atacado, preco_do_produtor)

