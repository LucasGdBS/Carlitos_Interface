
# Streamlit Components
import streamlit as st
from st_on_hover_tabs import on_hover_tabs as ht

# Page modules
import modules.funcionarios as func
import modules.clientes as clien
import modules.alimentos as alim
import modules.pedidos as pedi
import modules.atendentes as aten
import modules.motoqueiros as moto
import modules.gerentes as geren
import config.config as cfg



def app(page):
    st.set_page_config(layout="wide")
    st.markdown('<style>' + open('../style.css').read() + '</style>', unsafe_allow_html=True)
    with st.sidebar:    
        tabs = ht (tabName=['Funcionarios', 'Atendentes', 'Motoqueiros', 'Gerentes', 'Clientes', 'Alimentos', 'Pedidos'], 
                            iconName=['👨‍💼', '☎️', '🏍️', '‍💼', '🧑', '🍔', '🧾'], default_choice=page)
    if tabs =='Funcionarios':
        cfg.set_page(0, page)
        func.page_funcionario()

    elif tabs == 'Atendentes':
        cfg.set_page(1, page)
        aten.page_atendente()

    elif tabs == 'Motoqueiros':
        cfg.set_page(2, page)
        moto.page_motoqueiro()

    elif tabs == 'Gerentes':
        cfg.set_page(3, page)
        geren.page_gerente()

    elif tabs == 'Clientes':
        cfg.set_page(4, page)
        clien.page_cliente()

    elif tabs == 'Alimentos':
        cfg.set_page(5, page)
        alim.page_alimento()

    elif tabs == 'Pedidos':
        cfg.set_page(6, page)
        pedi.page_pedido()


if __name__ == '__main__':
    page = cfg.get_page()
    app(page)
