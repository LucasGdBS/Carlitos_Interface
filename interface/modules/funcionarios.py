import streamlit as st
import pandas as pd
import numpy as np


def page_funcionario():
    st.title("👨‍💼 Funcionarios")
    st.markdown("<br>", unsafe_allow_html=True)
    

    with st.form("cadastro_funcionarios", clear_on_submit=True):
        st.subheader("Cadastro de Funcionarios")

        cols = st.columns(2)

        with cols[0]:
            nome = st.text_input("Nome")
            cpf = st.text_input("CPF")

        with cols[1]:
            salario = st.text_input("Salario")
            cargo = st.text_input("Cargo")

        
        st.markdown("<br>", unsafe_allow_html=True)

        if st.form_submit_button("Cadastrar"):
            st.write("Funcionario cadastrado com sucesso")
        


    st.markdown("<br>", unsafe_allow_html=True)
    st.subheader("Lista de Funcionarios")


    sample_data = [
        {
            "nome": "João",
            "cpf": "123.456.789-00",
            "salario": "R$ 1.500,00",
            "cargo": "Atendente",
        },
        {
            "nome": "Maria",
            "cpf": "987.654.321-00",
            "salario": "R$ 2.500,00",
            "cargo": "Gerente",
        },
        {
            "nome": "José",
            "cpf": "456.789.123-00",
            "salario": "R$ 1.800,00",
            "cargo": "Motoqueiro",
        },
        {
            "nome": "Ana",
            "cpf": "654.321.987-00",
            "salario": "R$ 2.000,00",
            "cargo": "Atendente",
        },
    ]


    df_func = pd.DataFrame(sample_data)
    df_func.columns = ["Nome", "CPF", "Salario", "Cargo"]

    st.dataframe(df_func, hide_index=True, use_container_width=True)   
    