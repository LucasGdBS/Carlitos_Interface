import streamlit as st
from st_on_hover_tabs import on_hover_tabs as ht

# Importing page modules
import modules.funcionarios as func
import modules.clientes as clien
import modules.alimentos as alim
import modules.pedidos as pedi
import modules.atendentes as aten
import modules.motoqueiros as moto
import modules.gerentes as geren
import config.config as config



def app(page):
    st.set_page_config(layout="wide")
    st.markdown('<style>' + open('../style.css').read() + '</style>', unsafe_allow_html=True)
    with st.sidebar:    
        tabs = ht (tabName=['Funcionarios', 'Atendentes', 'Motoqueiros', 'Gerentes', 'Clientes', 'Alimentos', 'Pedidos'], 
                            iconName=['👨‍💼', '☎️', '🏍️', '‍💼', '🧑', '🍔', '🧾'], default_choice=page)
        

    if tabs =='Funcionarios':
        config.set_page(0, config.get_page())
        func.page_funcionario()

    elif tabs == 'Atendentes':
        config.set_page(1, config.get_page())
        aten.page_atendente()

    elif tabs == 'Motoqueiros':
        config.set_page(2, config.get_page())
        moto.page_motoqueiro()

    elif tabs == 'Gerentes':
        config.set_page(3, config.get_page())
        geren.page_gerente()

    elif tabs == 'Clientes':
        config.set_page(4, config.get_page())
        clien.page_cliente()

    elif tabs == 'Alimentos':
        config.set_page(5, config.get_page())
        alim.page_alimento()

    elif tabs == 'Pedidos':
        config.set_page(6, config.get_page())
        pedi.page_pedido()


page = config.get_page()
app(page)

