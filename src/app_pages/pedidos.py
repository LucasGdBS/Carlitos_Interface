import streamlit as st
import pandas as pd
from utils.page_modules import clear_input
# ! Mudar o import pras funções dos pedidos
# from utils.func_modules import fetch_funcionario, fetch_funcionario_by_cpf, fetch_funcionario_by_nome, create_funcionario, edit_funcionario_by_cpf, delete_funcionario



# * Página dos Pedidos
def page_pedido():
    st.title("🧾 Pedidos")
    st.markdown("<br>", unsafe_allow_html=True)


    # * Registrar Pedido

    with st.form("registrar_pedido", clear_on_submit= True):
        st.subheader("Registrar Pedido")

        # ! Alterar para dados do pedido
        # cols = st.columns(3)
        # with cols[0]:
        #     cpf = st.text_input("CPF")
        # with cols[1]:
        #     nome = st.text_input("Nome")
        # with cols[2]:
        #     salario = st.text_input("Salario")
        
        
        col_space, col1, col2 = st.columns([7, 1, 1], gap="small")

        # with col1:
        #     if st.form_submit_button("Registro", use_container_width=True):
        #         # ! Alterar pra função de registrar pedido
        #         new_func = create_funcionario(cpf, nome, salario)
        #         if new_func:
        #             st.toast("Pedido registrado com sucesso", icon="🎉")
        #         else:
        #             st.toast("Erro ao registrar um pedido", icon="⚠️")
        # with col2:
        #     if st.form_submit_button("Cancelar", type="primary", use_container_width=True):
        #         pass

  
  
    st.markdown("<br>", unsafe_allow_html=True)
    st.subheader("Lista dos Pedidos")


    if "search" not in st.session_state:
        st.session_state.search = "id"


    col1, col2, col3 = st.columns([8, 1, 1])
    with col1:
        id_func = st.text_input("ID do pedido", label_visibility="collapsed", placeholder=f"{st.session_state.search} do pedido", key="search_input")
    
    with col2:
        if st.button("Buscar", use_container_width=True, key="bottom_search_button"):
            pass
    with col3:
        st.button("Limpar", on_click=clear_input, use_container_width=True)
        

    # * Buscar por id do pedido ou exibir todos
    # ! Alterar pra as funções de pedidos
    # if id_func:
    #     if st.session_state.search == "id":
    #         data_func = fetch_funcionario_by_nome(id_func)
    #         df_func = pd.DataFrame(data_func)
    # else:
    #     data_func = fetch_funcionario()
    #     df_func = pd.DataFrame(data_func)

    # if data_func == []:
    #     st.error("Nenhum funcionário encontrado")
    # else:
    #     df_func.columns = ["CPF", "Nome", "Salário"]
    #     st.dataframe(df_func, hide_index=True, use_container_width=True)   
        
