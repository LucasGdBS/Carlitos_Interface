import streamlit as st
import pandas as pd


def page_ingrediente():
    st.title("🍔 Ingredientes")
    st.markdown("<br>", unsafe_allow_html=True)
    
    with st.form("cadastro_alimento", clear_on_submit=True):
        st.subheader("Cadastro de Alimentos")

        cols = st.columns(2)

        with cols[0]:
            nome = st.text_input("Nome")
            dt_validade = st.date_input("Data de Validade", value=None)
            quantidade = st.number_input("Quantidade", value=None)

        with cols[1]:
            valor = st.number_input("Valor", value=None)
            codigo = st.text_input("Codigo")
            tipo = st.text_input("Tipo")
        

        
        st.markdown("<br>", unsafe_allow_html=True)

        if st.form_submit_button("Cadastrar"):
            st.write("Alimento cadastrado com sucesso")
        


    st.markdown("<br>", unsafe_allow_html=True)
    st.subheader("Lista de Alimentos")


    sample_data = [
        {
            "nome": "X-Burguer",
            "dt_validade": "01/01/2022",
            "quantidade": 10,
            "valor": 10.00,
            "codigo": "123",
            "tipo": "Lanche",
        },
        {
            "nome": "X-Salada",
            "dt_validade": "01/01/2022",
            "quantidade": 10,
            "valor": 10.00,
            "codigo": "123",
            "tipo": "Lanche",
        },
        {
            "nome": "X-Bacon",
            "dt_validade": "01/01/2022",
            "quantidade": 10,
            "valor": 10.00,
            "codigo": "123",
            "tipo": "Lanche",
        },
        {
            "nome": "X-Tudo",
            "dt_validade": "01/01/2022",
            "quantidade": 10,
            "valor": 10.00,
            "codigo": "123",
            "tipo": "Lanche",
        }
    ]


    df_alimento = pd.DataFrame(sample_data)
    df_alimento.columns = ["Nome", "Data de Validade", "Quantidade", "Valor", "Codigo", "Tipo"]
    
    st.dataframe(df_alimento, hide_index=True, use_container_width=True)   
    