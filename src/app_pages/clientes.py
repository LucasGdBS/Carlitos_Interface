import streamlit as st
import pandas as pd


def page_cliente():
    st.title("👨 Clientes")
    st.markdown("<br>", unsafe_allow_html=True)
    
    with st.form("cadastro_clientes", clear_on_submit=True):
        st.subheader("Cadastro de Clientes")

        cols = st.columns(3)

        with cols[0]:
            nome = st.text_input("Nome")
            telefone = st.text_input("Telefone")
            cep = st.text_input("CEP")
            

        with cols[1]:
            rua = st.text_input("Rua")
            bairro = st.text_input("Bairro")
        
        with cols[2]:
            numero = st.text_input("Numero")
            complemento = st.text_input("Complemento")
          


        
        st.markdown("<br>", unsafe_allow_html=True)

        if st.form_submit_button("Cadastrar"):
            st.write("Cliente cadastrado com sucesso")
        


    st.markdown("<br>", unsafe_allow_html=True)
    st.subheader("Lista de Clientes")


    sample_data = [
        {
            "nome": "João da Silva",
            "telefone": "(11) 99999-9999",
            "cep": "12345-678",
            "rua": "Rua dos Bobos",
            "bairro": "Vila Esperança",
            "numero": "123",
            "complemento": "Apto 12"
        },
        {
            "nome": "Maria da Silva",
            "telefone": "(11) 99999-9999",
            "cep": "12345-678",
            "rua": "Rua dos Bobos",
            "bairro": "Vila Esperança",
            "numero": "123",
            "complemento": "Apto 12"
        },
        {
            "nome": "José da Silva",
            "telefone": "(11) 99999-9999",
            "cep": "12345-678",
            "rua": "Rua dos Bobos",
            "bairro": "Vila Esperança",
            "numero": "123",
            "complemento": "Apto 12"
        },
        {
            "nome": "Ana da Silva",
            "telefone": "(11) 99999-9999",
            "cep": "12345-678",
            "rua": "Rua dos Bobos",
            "bairro": "Vila Esperança",
            "numero": "123",
            "complemento": "Apto 12"
        }
    ]


    df_cliente = pd.DataFrame(sample_data)
    df_cliente.columns = ["Nome", "Telefone", "CEP", "Rua", "Bairro", "Numero", "Complemento"]
    
    st.dataframe(df_cliente, hide_index=True, use_container_width=True)   
    