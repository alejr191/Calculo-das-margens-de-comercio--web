import streamlit as st

# Configuração do título e das páginas
st.title("Cálculo de Margens Comerciais")
st.sidebar.title("Selecione a Página")
page = st.sidebar.selectbox("Escolha a margem:", ["Margem Absoluta", "Margem Relativa"])

if page == "Margem Absoluta":
    st.header("Cálculo da Margem Absoluta")
    pv = st.number_input('Informe o preço do Varejo:', min_value=0.0, format="%.2f")
    pa = st.number_input('Informe o preço do Atacado:', min_value=0.0, format="%.2f")
    pp = st.number_input('Informe o preço do Produtor:', min_value=0.0, format="%.2f")

    if st.button("Calcular"):
        margem_total = pv - pp
        margem_atacado = pa - pp
        margem_varejo = pv - pa

        st.write(f"Margem Total: {margem_total:.2f}")
        st.write(f"Margem do Atacado: {margem_atacado:.2f}")
        st.write(f"Margem do Varejo: {margem_varejo:.2f}")

elif page == "Margem Relativa":
    st.header("Cálculo da Margem Relativa")
    preco_do_varejo = st.number_input('Informe o preço do varejo:', min_value=0.0, format="%.2f")
    preco_do_atacado = st.number_input('Informe o preço do atacado:', min_value=0.0, format="%.2f")
    preco_do_produtor = st.number_input('Informe o preço do produtor:', min_value=0.0, format="%.2f")

    if st.button("Calcular"):
        margem_total = (preco_do_varejo - preco_do_produtor) / preco_do_varejo * 100
        margem_varejo = (preco_do_varejo - preco_do_atacado) / preco_do_varejo * 100
        margem_atacado = (preco_do_atacado - preco_do_produtor) / preco_do_varejo * 100
        margem_produtor = (preco_do_produtor / preco_do_varejo) * 100

        st.write(f"Margem do Varejo: {margem_varejo:.2f}%")
        st.write(f"Margem do Atacado: {margem_atacado:.2f}%")
        st.write(f"Margem do Produtor: {margem_produtor:.2f}%")
        st.write(f"Margem Total: {margem_total:.2f}%")

