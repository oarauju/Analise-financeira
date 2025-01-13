import streamlit as st
import pandas as pd
import plotly.graph_objects as go

# Configurações iniciais
st.set_page_config(page_title="Saúde Financeira para Empresas", layout="wide")

# Função para calcular os indicadores
def calcular_indicadores(receita, deducoes, custos, despesas, impostos, periodos_anteriores):
    receita_liquida = receita - deducoes
    lucro_bruto = receita_liquida - custos
    lucro_liquido = lucro_bruto - despesas - impostos
    crescimento = ((receita_liquida - periodos_anteriores) / periodos_anteriores) * 100 if periodos_anteriores else 0
    margem_lucro = (lucro_liquido / receita_liquida) * 100 if receita_liquida > 0 else 0
    return {
        "Receita Líquida": receita_liquida,
        "Lucro Bruto": lucro_bruto,
        "Lucro Líquido": lucro_liquido,
        "Crescimento (%)": crescimento,
        "Margem de Lucro (%)": margem_lucro,
        "Impostos Pagos": impostos,
    }

# Simulação de entrada de dados (ajuste para conectar ao banco de dados)
st.sidebar.title("Parâmetros Financeiros")
receita = st.sidebar.number_input("Receita Bruta", value=500000.0, step=5000.0)
deducoes = st.sidebar.number_input("Deduções (Impostos/Descontos)", value=50000.0, step=500.0)
custos = st.sidebar.number_input("Custos Totais", value=200000.0, step=1000.0)
despesas = st.sidebar.number_input("Despesas Operacionais", value=100000.0, step=500.0)
impostos = st.sidebar.number_input("Impostos Totais", value=50000.0, step=500.0)
periodos_anteriores = st.sidebar.number_input("Receita do Período Anterior", value=450000.0, step=5000.0)

# Cálculo dos indicadores
indicadores = calcular_indicadores(receita, deducoes, custos, despesas, impostos, periodos_anteriores)

# Título
st.title("Análise Financeira Empresarial")

# Indicadores principais com ícones
col1, col2, col3, col4 = st.columns(4)
col1.metric("Receita Líquida", f"R$ {indicadores['Receita Líquida']:,.2f}")
col2.metric("Lucro Líquido", f"R$ {indicadores['Lucro Líquido']:,.2f}")
col3.metric("Crescimento (%)", f"{indicadores['Crescimento (%)']:.2f}%", delta=f"{indicadores['Crescimento (%)']:.2f}")
col4.metric("Impostos Pagos", f"R$ {indicadores['Impostos Pagos']:,.2f}")

# Gráficos
st.markdown("### Comparação de Desempenho")
fig = go.Figure()
fig.add_trace(go.Bar(x=["Receita Líquida", "Lucro Bruto", "Lucro Líquido"], 
                     y=[indicadores['Receita Líquida'], indicadores['Lucro Bruto'], indicadores['Lucro Líquido']], 
                     text=[indicadores['Receita Líquida'], indicadores['Lucro Bruto'], indicadores['Lucro Líquido']],
                     textposition='auto', marker_color=['#4caf50', '#2196f3', '#f44336']))
fig.update_layout(title="Indicadores Financeiros", template="simple_white")
st.plotly_chart(fig, use_container_width=True)

# Explicação dos indicadores
st.markdown("### Explicação dos Indicadores")
st.write("""
- **Receita Líquida**: Total de receita gerada pela empresa após descontos e deduções.
- **Lucro Líquido**: Resultado final após todas as despesas e impostos.
- **Crescimento**: Percentual de aumento ou diminuição da receita líquida em relação ao período anterior.
- **Impostos Pagos**: Total pago em impostos no período.
""")

# Rodapé
st.markdown("---")
st.write("Desenvolvido para empresas que buscam uma visão detalhada de sua saúde financeira.")
