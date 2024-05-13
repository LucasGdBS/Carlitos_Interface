import streamlit as st
import pandas as pd
import numpy as np


def page_motoqueiro():
    st.title("🛵 Motoqueiros")
    st.markdown("<br>", unsafe_allow_html=True)
    

    st.subheader("Lista de motoqueiros")


    sample_data = [
        {
            "nome": "João",
            "cpf": "123.456.789-00",
            "salario": "R$ 1.500,00",
            "cargo": "Motoqueiro",
        },
        {
            "nome": "José",
            "cpf": "456.789.123-00",
            "salario": "R$ 1.800,00",
            "cargo": "Motoqueiro",
        },
        {
            "nome": "Pedro",
            "cpf": "789.123.456-00",
            "salario": "R$ 1.700,00",
            "cargo": "Motoqueiro",
        },
        {
            "nome": "Paulo",
            "cpf": "321.654.987-00",
            "salario": "R$ 1.900,00",
            "cargo": "Motoqueiro",
        }
    ]


    df_mot = pd.DataFrame(sample_data)
    df_mot.columns = ["Nome", "CPF", "Salario", "Cargo"]

    st.dataframe(df_mot, hide_index=True, use_container_width=True)   
    