import streamlit as st
from st_on_hover_tabs import on_hover_tabs as ht
import modules.funcionarios as func
import modules.clientes as clien
import modules.alimentos as alim
import modules.pedidos as pedi

def app():

    st.set_page_config(layout="wide")
    st.markdown('<style>' + open('../style.css').read() + '</style>', unsafe_allow_html=True)


    with st.sidebar:    
        tabs = ht (tabName=['Funcionarios', 'Atendentes', 'Motoqueiros', 'Gerentes', 'Clientes', 'Alimentos', 'Pedidos'], 
                            iconName=['👨‍💼', '☎️', '🏍️', '‍💼', '🧑', '🍔', '🧾'], default_choice=0)

    if tabs =='Funcionarios':
        func.page_funcionario()

    elif tabs == 'Atendentes':
        st.title("Navigation Bar")
        st.write('Name of option is {}'.format(tabs))
    
    elif tabs == 'Motoqueiros':
        st.title("Navigation Bar")
        st.write('Name of option is {}'.format(tabs))
    
    elif tabs == 'Gerentes':
        st.title("Navigation Bar")
        st.write('Name of option is {}'.format(tabs))
    
    elif tabs == 'Clientes':
        clien.page_cliente()
    
    elif tabs == 'Alimentos':
        alim.page_alimento()
    
    elif tabs == 'Pedidos':
        pedi.page_pedido()
    


app()