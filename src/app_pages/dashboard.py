import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from utils.func_modules import fetch_funcionario
from utils.dash_modules import faturamento_diario, faturamento_mensal, faturamento_anual, clientes_bairro, forma_pagamento, produtos_vendidos, pedidos_por_turno
from utils.dash_modules import funcionarios_salario_media, atendentes_mais_vendas, produtos_3ingredientes, ingredientes_vencimento, ingredientes_mais_utilizados



# * Página dos Dashboards
def page_dashboard():
    st.title("📊 Dashboard")
    st.markdown("<br>", unsafe_allow_html=True)


    if "options" not in st.session_state:
        st.session_state.options = "Faturamento"
    st.radio("Categorias:", ["Faturamento", "Funcionários", "Produtos", "Clientes"], key="options", horizontal=True)
    st.markdown("<br>", unsafe_allow_html=True)


    # * Faturamento
    if st.session_state.options == "Faturamento":
        st.subheader("Faturamento Anual")
        fat_anual =  faturamento_anual()
        chart_anual = pd.DataFrame(fat_anual)
        chart_anual.columns = ["Ano", "Faturamento"]
        fig = px.bar(chart_anual, x="Ano", y="Faturamento", color="Faturamento", color_continuous_scale="Inferno")
        fig.update_layout(xaxis_type='category')
        st.plotly_chart(fig, use_container_width=True)


        col1, col2, col3 = st.columns([8, 1, 8])
        with col1:
            st.subheader("Faturamento Mensal")
            fat_mensal = faturamento_mensal()
            media = [i["faturamento_mensal"] for i in fat_mensal]
            chart_mensal = pd.DataFrame(fat_mensal)
            chart_mensal.columns = ["Mês", "Faturamento"]

            fig = px.line(chart_mensal, x="Mês", y="Faturamento")
            fig.add_hline(y=np.mean(media),  line_color="white", annotation_text="Média", annotation_position="top right", line_dash="dash")
            fig.update_traces(line=dict(color='#FF8B1F'))
            st.plotly_chart(fig, use_container_width=True)
            
        
        with col3:
            st.subheader("Faturamento Diário")
            fat_diario = faturamento_diario()
            media = [i["faturamento_diario"] for i in fat_diario]
            chart_diario = pd.DataFrame(fat_diario)
            chart_diario.columns = ["Dia", "Faturamento"]

            fig = px.line(chart_diario, x="Dia", y="Faturamento")
            fig.add_hline(y=np.mean(media),  line_color="white", annotation_text="Média", annotation_position="top right", line_dash="dash")
            fig.update_traces(line=dict(color='#FF8B1F'))
            st.plotly_chart(fig, use_container_width=True)





    # * Funcionários
    elif st.session_state.options == "Funcionários":
        st.subheader("Atendentes com Mais Vendas")
        atendentes_vendas = atendentes_mais_vendas()
        chart_atendentes_vendas = pd.DataFrame(atendentes_vendas)
        chart_atendentes_vendas.columns = ["CPF", "Nome", "Vendas"]
        st.dataframe(chart_atendentes_vendas, use_container_width=True, hide_index=True)


        st.subheader("Salários Acima da Média")
        salario_media = funcionarios_salario_media()
        chart_salario_media = pd.DataFrame(salario_media)
        chart_salario_media.columns = ["Funcionário", "Salário"]
        fig = px.bar(chart_salario_media, y="Salário", x="Funcionário", color="Salário", color_continuous_scale="Inferno")     

        funcionarios = fetch_funcionario()
        media = [i["salario"] for i in funcionarios]

        fig.add_hline(y=np.mean(media),  line_color="white", annotation_text="Média", annotation_position="top left", line_dash="dash")
        st.plotly_chart(fig, use_container_width=True)





    # * Produtos
    elif st.session_state.options == "Produtos":
        st.subheader("Produtos Mais Vendidos")
        prod_vend = produtos_vendidos()
        chart_prod_vend = pd.DataFrame(prod_vend)
        chart_prod_vend.columns = ["Produto", "Quantidade"]
        fig = px.bar(chart_prod_vend, y="Quantidade", x="Produto", color="Quantidade", color_continuous_scale="Inferno")
        st.plotly_chart(fig, use_container_width=True)
        
        st.subheader("Produtos com Mais de 3 Ingredientes")
        prod_3ing = produtos_3ingredientes()
        chart_prod_3ing = pd.DataFrame(prod_3ing)
        chart_prod_3ing.columns = ["Produto"]
        st.dataframe(chart_prod_3ing, use_container_width=True, hide_index=True)

        col1, col2 = st.columns([5,5])
        with col1:
            st.subheader("Ingredientes Mais Utilizados")
            ingred_mais = ingredientes_mais_utilizados()
            chart_ingred_mais = pd.DataFrame(ingred_mais)
            chart_ingred_mais.columns = ["Ingrediente", "Quantidade"]
            fig = px.pie(chart_ingred_mais, values="Quantidade", names="Ingrediente", color_discrete_sequence=px.colors.sequential.RdBu)
            st.plotly_chart(fig, use_container_width=True)
        with col2:  
            st.subheader("Ingredientes Próximos ao Vencimento")
            ingred_venc = ingredientes_vencimento()
            chart_ingred_venc = pd.DataFrame(ingred_venc)
            st.dataframe(chart_ingred_venc, use_container_width=True, hide_index=True)





    # * Clientes
    elif st.session_state.options == "Clientes":
        st.subheader("Clientes por Bairro")
        clien_bairro = clientes_bairro()
        chart_clien_bairro = pd.DataFrame(clien_bairro)
        chart_clien_bairro.columns = ["Bairro", "Clientes"]
        fig = px.bar(chart_clien_bairro, y="Clientes", x="Bairro", color="Clientes", color_continuous_scale="Inferno")
        st.plotly_chart(fig, use_container_width=True)


        col1, col2 = st.columns([5,5])
        with col1:
            st.subheader("Formas de Pagamento Mais Utilizadas")
            forma_pag = forma_pagamento()
            chart_forma_pag = pd.DataFrame(forma_pag)
            chart_forma_pag.columns = ["Forma de Pagamento", "Quantidade"]
            fig = px.pie(chart_forma_pag, values="Quantidade", names="Forma de Pagamento", color_discrete_sequence=px.colors.sequential.RdBu)
            st.plotly_chart(fig, use_container_width=True)
        with col2:
            st.subheader("Pedidos por Turno")
            ped_turno = pedidos_por_turno()
            chart_ped_turno = pd.DataFrame(ped_turno)
            chart_ped_turno.columns = ["Turno", "Pedidos"]
            fig = px.pie(chart_ped_turno, values="Pedidos", names="Turno", color_discrete_sequence=px.colors.sequential.RdBu)
            st.plotly_chart(fig, use_container_width=True)

    
