import streamlit as st
from st_pages import show_pages_from_config

st.set_page_config(page_title="CarlitosBD - Página Inicial", page_icon="🖥️")
show_pages_from_config()

st.header("CarlitosBD - Sistema de Gestão de Restaurante")
st.markdown('<style>' + open('./style.css').read() + '</style>', unsafe_allow_html=True)


st.write("Bem-vindo ao CarlitosBD, o sistema de gestão do Carlitos\
          Aqui você pode gerenciar seus funcionários, clientes, produtos e pedidos de forma simples e intuitiva.\
          Para começar, selecione uma das opções no menu lateral.")
st.image("images/Logo-Sistema1.jpeg")


