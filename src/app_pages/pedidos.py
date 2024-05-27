import streamlit as st
import pandas as pd
from utils.page_modules import clear_input
from utils.pedi_modules import fetch_pedido, fetch_pedido_by_id, fetch_pedido_by_name, fetch_pedido_resumo, fetch_pedido_resumo_by_atendente, create_pedido,  delete_pedido
from utils.clien_modules import fetch_cliente_by_telefone


# * Página dos Pedidos
def page_pedido():
    st.title("🧾 Pedidos")
    st.markdown("<br>", unsafe_allow_html=True)


    if "options" not in st.session_state:
        st.session_state.options = "cadastrar"
    st.radio("Operações:", ["cadastrar", "deletar"], key="options", horizontal=True)


    if st.session_state.options == "deletar":
        col1, col2, col3 = st.columns([8, 1, 1])
        with col1:
            id_pedido = st.text_input("ID do pedido", key="forms_input", placeholder="Número do pedido", label_visibility="collapsed")
            selected_pedido = fetch_pedido_by_id(id_pedido)
        with col2:
            if st.button("Buscar", use_container_width=True, key="top_search_button"):
                selected_pedido = fetch_pedido_by_id(id_pedido) 
        with col3:
            st.button("Limpar", on_click=clear_input, use_container_width=True, key="clear")
    

    count_pedido = fetch_pedido()
    count_cod_nota = pd.DataFrame(count_pedido)["codigoNotalFiscal"].max()+1
    count_num_pedido = pd.DataFrame(count_pedido)["numeroPedido"].max()+1


  
    
    # * Criar pedido
    if st.session_state.options == "cadastrar":
        with st.form("cadastrar_pedido", clear_on_submit= False):
            st.subheader("Cadastrar Pedido")

            cols = st.columns(2)
            with cols[0]:
                cod_nota = st.number_input("Código Nota Fiscal", value=count_cod_nota, disabled=True)
                num_pedido = st.number_input("Número do Pedido", value=count_num_pedido, disabled=True) 
                id_cliente = st.number_input("ID do Cliente", step=1)
                id_input = st.text_input("IDs dos Produtos", placeholder="Ex: 1, 2, 3") 
                cpf_atendente = st.text_input("CPF do Atendente")
            with cols[1]:
                dt_pedido = st.text_input("Data do Pedido", placeholder="aaaa-mm-dd")
                forma_pagamento = st.selectbox("Forma de Pagamento", ["dinheiro", "crédito", "débito", "pix"])
                taxa_entrega = st.number_input("Taxa de Entrega")
                desconto = st.number_input("Desconto")
                qntd_input = st.text_input("Quantidades dos Produtos", placeholder="Ex: 1, 2, 3")
            

            col_space, col1, col2 = st.columns([7, 1, 1], gap="small")

            with col1:
                if st.form_submit_button("Cadastrar", use_container_width=True):
                    new_pedido = create_pedido(cod_nota, num_pedido, id_cliente, id_input, cpf_atendente, dt_pedido, forma_pagamento, taxa_entrega, desconto, qntd_input)

                    if new_pedido == True:
                        st.toast(f"Pedido {num_pedido} cadastrado com sucesso", icon="🎉")
                    else:
                        st.toast(new_pedido, icon="⚠️")
            with col2:
                if st.form_submit_button("Cancelar", type='primary', use_container_width=True):
                    pass
    


    # * Deletar pedido
    if st.session_state.options == "deletar":

        if "deleted" not in st.session_state:
            st.session_state.deleted = False
        if st.session_state.deleted:
            st.session_state.deleted = False

            st.toast("Pedido deletado com sucesso", icon="🎉")
        

        if selected_pedido:
            with st.form("deletar_pedido", clear_on_submit=True):
                st.subheader("Deletar pedido")


                info_pedido = fetch_pedido_resumo(id_pedido)
                info_pedido_df = pd.DataFrame([info_pedido])
                info_pedido_df.columns = ["Número do Pedido", "Valor Total(R$)", "Nome do Cliente", "Produtos"]
                st.dataframe(info_pedido_df, hide_index=True, use_container_width=True)


                col_space, col1, col2 = st.columns([7, 1, 1], gap="small")

                with col1:
                    if st.form_submit_button("Deletar", use_container_width=True):
                        delete_clien = delete_pedido(id_pedido)
                        if delete_clien:
                            st.session_state.deleted = True
                            st.rerun()
                        else:
                            st.toast("Erro ao deletar pedido", icon="⚠️")
                with col2:
                    if st.form_submit_button("Cancelar",type='primary', use_container_width=True):
                        pass

        elif selected_pedido == [] and id_pedido != "" and st.session_state.deleted == True:
            st.toast("Pedido não encontrado", icon="⚠️")       
    



    # * Listar os pedidos
    st.markdown("<br>", unsafe_allow_html=True)
    st.subheader("Lista de Pedidos")


    # * Exibir pedidos complestos ou resumidos
    if "mode" not in st.session_state:
        st.session_state.mode = "detalhado"
    st.radio("Modo de exibição:", ["detalhado", "resumo"], key="mode", horizontal=True)


    if "search" not in st.session_state:
        st.session_state.search = "nome do cliente"
    st.radio("Buscar por:", ["nome do cliente", "número do pedido"], key="search", horizontal=True)

    col1, col2, col3 = st.columns([8, 1, 1])
    with col1:
        atendente = st.text_input("ID do Pedido", label_visibility="collapsed", placeholder=f"{st.session_state.search}", key="search_input")
    with col2:
        if st.button("Buscar", use_container_width=True, key="bottom_search_button"):
            pass
    with col3:
        st.button("Limpar", on_click=clear_input, use_container_width=True)


    # * Exibir pedidos detalhados 
    if st.session_state.mode == "detalhado":
        if atendente:
            if st.session_state.search == "nome do cliente":
                data_pedido = fetch_pedido_by_name(atendente)
                df_pedido = pd.DataFrame(data_pedido)
            if st.session_state.search == "número do pedido":
                st.write(st.session_state.search)
                data_pedido = fetch_pedido_by_id(atendente)
                df_pedido = pd.DataFrame(data_pedido)
        else:
            data_pedido = fetch_pedido()
            df_pedido = pd.DataFrame(data_pedido)


        if data_pedido == []:
            st.error("Nenhum pedido encontrado")
        else:
            df_pedido.columns = ["Código Nota Fiscal", "Número do Pedido", "ID do Cliente", "Nome do Cliente", "ID do Produto", "Nome do Produto", "CPF do Atendente", "Valor Total(R$)", "Valor sem Desconto", "Desconto(R$)", "Data do Pedido", "Forma de Pagamento", "Taxa de Entrega(R$)", "Desconto(%)", "Quantidade do Produto"]
            st.dataframe(df_pedido, hide_index=True, use_container_width=True)


    # * Exibir pedidos resumidos
    if st.session_state.mode == "resumo":
        if atendente:
            if st.session_state.search == "nome do cliente":
                data_pedido = fetch_pedido_resumo_by_atendente(atendente)
                df_pedido = pd.DataFrame(data_pedido)
            if st.session_state.search == "número do pedido":
                data_pedido = fetch_pedido_resumo(atendente)
                df_pedido = pd.DataFrame([data_pedido])


            if data_pedido == []:
                st.error("Nenhum pedido encontrado")
            else:
                df_pedido.columns = ["Número do Pedido", "Valor Total(R$)", "Nome do Cliente", "Produtos"]
                st.dataframe(df_pedido, hide_index=True, use_container_width=True)
        else:
            st.warning(f"Digite o {st.session_state.search} do pedido para exibir os resultados")


