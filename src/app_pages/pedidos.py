import streamlit as st
import pandas as pd
from utils.page_modules import clear_input
# ! Mudar o import pras funções dos pedidos
# from utils.func_modules import fetch_funcionario, fetch_funcionario_by_cpf, fetch_funcionario_by_nome, create_funcionario, edit_funcionario_by_cpf, delete_funcionario



# * Página dos Pedidos
def page_pedido():
    st.title("🧾 Pedidos")
    st.markdown("<br>", unsafe_allow_html=True)


    