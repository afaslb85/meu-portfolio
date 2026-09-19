
import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Análise do Portfólio de Investimentos", layout="wide")
st.title("📊 Análise do Portfólio de Investimentos")

# Upload do ficheiro (CSV ou Excel)
uploaded_file = st.sidebar.file_uploader("Carrega o teu ficheiro", type=["csv", "xlsx", "xls"])

if uploaded_file is not None:
    try:
        # Lê Excel (.xlsx / .xls) ou CSV
        if uploaded_file.name.endswith(('.xlsx', '.xls')):
            df = pd.read_excel(uploaded_file)
        else:
            df = pd.read_csv(uploaded_file)

        st.success("Ficheiro carregado com sucesso!")
        
        # Exibe a tabela com os teus dados da XTB
        st.subheader("📋 Dados do Extrato")
        st.dataframe(df)

    except Exception as e:
        st.error(f"Erro ao processar o ficheiro: {e}")
else:
    st.info("Por favor, carrega um ficheiro na barra lateral para começar.")
