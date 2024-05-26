
# Streamlit Components
import streamlit as st
from st_on_hover_tabs import on_hover_tabs as ht

# App pages
import app_pages.funcionarios as func
import app_pages.clientes as clien
import app_pages.ingredientes as ingred
import app_pages.pedidos as pedi
import app_pages.atendentes as aten
import app_pages.motoqueiros as moto
import app_pages.gerentes as geren
import app_pages.produtos as prod
import app_pages.dashboard as dash

# Config files
from config import config as cfg


def app(page):
    st.set_page_config(layout="wide")
    st.markdown('<style>' + open('./assets/style.css').read() + '</style>', unsafe_allow_html=True)


    with st.sidebar:    
        tabs = ht (tabName=['Dashboard', 'Funcionarios', 'Atendentes', 'Motoqueiros', 'Gerentes', 'Clientes', 'Ingredientes', 'Produtos', 'Pedidos'], 
                            iconName=['📊', '👨‍💼', '☎️', '🏍️', '‍💼', '🧑', '🥦', '🍔', '🧾'], default_choice=page)
        
    if tabs == 'Dashboard':
        cfg.set_page(0, page)
        dash.page_dashboard()
        
    elif tabs =='Funcionarios':
        cfg.set_page(1, page)
        func.page_funcionario()

    elif tabs == 'Atendentes':
        cfg.set_page(2, page)
        aten.page_atendente()

    elif tabs == 'Motoqueiros':
        cfg.set_page(3, page)
        moto.page_motoqueiro()

    elif tabs == 'Gerentes':
        cfg.set_page(4, page)
        geren.page_gerente()

    elif tabs == 'Clientes':
        cfg.set_page(5, page)
        clien.page_cliente()

    elif tabs == 'Ingredientes':
        cfg.set_page(6, page)
        ingred.page_ingrediente()
    
    elif tabs == 'Produtos':
        cfg.set_page(7, page)
        prod.page_produto()

    elif tabs == 'Pedidos':
        cfg.set_page(8, page)
        pedi.page_pedido()


if __name__ == '__main__':
    page = cfg.get_page()
    app(page)
