import streamlit as st
import pandas as pd
import numpy as np


def page_atendente():
    st.title("☎️ Atendentes")
    st.markdown("<br>", unsafe_allow_html=True)
    

    st.subheader("Lista de Atendentes")


    sample_data = [
        {
            "nome": "João",
            "cpf": "123.456.789-00",
            "salario": "R$ 1.500,00",
            "cargo": "Atendente",
        },
        {
            "nome": "Ana",
            "cpf": "654.321.987-00",
            "salario": "R$ 2.000,00",
            "cargo": "Atendente",
        },
        {
            "nome": "Maria",
            "cpf": "987.654.321-00",
            "salario": "R$ 2.500,00",
            "cargo": "Atendente",
        },
        {
            "nome": "José",
            "cpf": "456.789.123-00",
            "salario": "R$ 1.800,00",
            "cargo": "Atendente",
        }
    ]


    df_atend = pd.DataFrame(sample_data)
    df_atend.columns = ["Nome", "CPF", "Salario", "Cargo"]

    st.dataframe(df_atend, hide_index=True, use_container_width=True)   
    