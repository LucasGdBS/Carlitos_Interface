import streamlit as st
import pandas as pd
from utils.moto_modules import fetch_motoqueiro


# * Página de Motoqueiros
def page_motoqueiro():
    st.title("🛵 Motoqueiros")
    st.markdown("<br>", unsafe_allow_html=True)
    

    st.subheader("Lista de motoqueiros")


    data_func = fetch_motoqueiro()
    df_func = pd.DataFrame(data_func)

    if data_func == []:
        st.error("Nenhum motoqueiro encontrado")
    else:
        df_func.columns = ["CPF", "Nome", "Salário", "CPF Gerente-Motoqueiro", "Nome Gerente-Motoqueiro"]
        st.dataframe(df_func, hide_index=True, use_container_width=True)   


    