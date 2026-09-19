import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Análise de Portfólio", layout="wide")
st.title("📊 Análise do Portfólio de Investimentos")

# Upload do ficheiro CSV
uploaded_file = st.sidebar.file_uploader("Carrega o teu ficheiro", type=["csv", "xlsx", "xls"])

if uploaded_file is not None:
    df = pd.read_excel(uploaded_file) if uploaded_file.name.endswith(('.xlsx', '.xls')) else pd.read_csv(uploaded_file)

    
    # Cálculo do valor investido por posição
    df['total_investido'] = df['quantidade'] * df['preco_medio']
    
    # Métricas Globais
    total_geral = df['total_investido'].sum()
    total_ativos = len(df['ticker'].unique())
    
    col1, col2 = st.columns(2)
    col1.metric("Valor Total Investido", f"{total_geral:,.2f} €")
    col2.metric("Total de Ativos", total_ativos)
    
    st.markdown("---")
    
    # Tabela com dados carregados
    st.subheader("📋 Posições")
    st.dataframe(df, use_container_width=True)
    
    # Visualização de Alocação
    st.subheader("📈 Alocação do Portfólio")
    
    tipo_grafico = st.radio("Escolha o tipo de gráfico:", ["Donut Chart", "Treemap"], horizontal=True)
    dimensao = st.selectbox("Analisar quebra por:", ["tipo_ativo", "setor", "pais"])
    
    if tipo_grafico == "Donut Chart":
        fig = px.pie(
            df, 
            values='total_investido', 
            names=dimensao, 
            hole=0.4,
            title=f"Distribuição por {dimensao.replace('_', ' ').capitalize()}"
        )
    else:
        fig = px.treemap(
            df, 
            path=[dimensao, 'ticker'], 
            values='total_investido',
            title=f"Treemap por {dimensao.replace('_', ' ').capitalize()}"
        )
        
    st.plotly_chart(fig, use_container_width=True)
else:
    st.info("Por favor, carrega um ficheiro CSV na barra lateral para começar.")
