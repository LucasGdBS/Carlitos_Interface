import streamlit as st
import pandas as pd
import numpy as np


def page_gerente():
    st.title("💼 Gerentes")
    st.markdown("<br>", unsafe_allow_html=True)
    

    st.subheader("Lista de Gerentes")


    sample_data = [
        {
            "nome": "Maria",
            "cpf": "987.654.321-00",
            "salario": "R$ 2.500,00",
            "cargo": "Gerente",
        },
        {
            "nome": "Paulo",
            "cpf": "321.654.987-00",
            "salario": "R$ 2.000,00",
            "cargo": "Gerente",
        },
        {
            "nome": "Pedro",
            "cpf": "789.123.456-00",
            "salario": "R$ 2.100,00",
            "cargo": "Gerente",
        },
        {
            "nome": "João",
            "cpf": "123.456.789-00",
            "salario": "R$ 2.200,00",
            "cargo": "Gerente",
        }
    ]


    df_ger = pd.DataFrame(sample_data)
    df_ger.columns = ["Nome", "CPF", "Salario", "Cargo"]

    st.dataframe(df_ger, hide_index=True, use_container_width=True)   
    