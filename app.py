
import streamlit as st
import pandas as pd
import plotly.express as px

# Título do Dashboard
st.set_page_config(page_title="Dashboard Barbearia 2025", layout="wide")
st.title("✂️ Dashboard de Cortes da Barbearia - 2025")

# Dados fornecidos
data = {
    'Mês': ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho',
            'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro'],
    'Cortes': [18, 37, 28, 25, 32, 45, 48, 22, 24, 29, 35, 55]
}
df = pd.DataFrame(data)

# Definir meses de pico
pico_meses = ['Fevereiro', 'Junho', 'Julho', 'Dezembro']
df['Pico'] = df['Mês'].apply(lambda x: 'Sim' if x in pico_meses else 'Não')

# Seletor interativo de meses
st.sidebar.header('Filtro de Meses')
meses_selecionados = st.sidebar.multiselect(
    'Selecione os meses para visualizar',
    options=df['Mês'].tolist(),
    default=df['Mês'].tolist()
)

df_filtrado = df[df['Mês'].isin(meses_selecionados)]

# KPIs
st.subheader("Indicadores Principais (KPIs)")
col1, col2, col3, col4 = st.columns(4)

with col1:
    total_cortes = df_filtrado['Cortes'].sum()
    st.metric(label="Total de Cortes", value=f"{total_cortes}")

with col2:
    media_cortes = df_filtrado['Cortes'].mean()
    st.metric(label="Média Mensal de Cortes", value=f"{media_cortes:.2f}")

with col3:
    mes_maior_corte = df_filtrado.loc[df_filtrado['Cortes'].idxmax()]
    st.metric(label="Mês com Mais Cortes", value=f"{mes_maior_corte['Mês']} ({mes_maior_corte['Cortes']})")

with col4:
    mes_menor_corte = df_filtrado.loc[df_filtrado['Cortes'].idxmin()]
    st.metric(label="Mês com Menos Cortes", value=f"{mes_menor_corte['Mês']} ({mes_menor_corte['Cortes']})")

# Gráfico de Linhas - Evolução Mensal
st.subheader("Evolução Mensal de Cortes")
fig_linha = px.line(df_filtrado, x='Mês', y='Cortes', markers=True,
                    title='Evolução Mensal de Cortes em 2025',
                    color_discrete_sequence=px.colors.qualitative.Pastel)
fig_linha.update_traces(line_color='#6A0572') # Cor da linha
fig_linha.update_layout(hovermode="x unified")
st.plotly_chart(fig_linha, use_container_width=True)

# Gráfico de Barras - Comparação Mês a Mês
st.subheader("Comparação Mês a Mês")
fig_barra = px.bar(df_filtrado, x='Mês', y='Cortes',
                   title='Comparação de Cortes Mês a Mês em 2025',
                   color='Pico', color_discrete_map={'Sim': '#FF6B6B', 'Não': '#4ECDC4'})
fig_barra.update_layout(hovermode="x unified")
st.plotly_chart(fig_barra, use_container_width=True)

# Comentários no código (já incluídos acima e ao longo do arquivo)

# Design limpo e cores agradáveis (definidos nas configurações do Streamlit e nos gráficos)



