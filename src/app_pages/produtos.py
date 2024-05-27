import streamlit as st
import pandas as pd
from utils.page_modules import clear_input
from utils.prod_modules import fetch_produto, fetch_produto_by_id, fetch_produto_by_nome, create_produto, edit_produto, delete_produto



# * Página de Produtos
def page_produto():
    st.title("🍔 Produtos")
    st.markdown("<br>", unsafe_allow_html=True)


    if "options" not in st.session_state:
        st.session_state.options = "cadastrar"
    st.radio("Operações:", ["cadastrar", "editar", "deletar"], key="options", horizontal=True)


    if st.session_state.options != "cadastrar":
        col1, col2, col3 = st.columns([8, 1, 1])
        with col1:
            id_prod = st.text_input("ID do produto", key="forms_input", placeholder="código do produto", label_visibility="collapsed")
            selected_prod = fetch_produto_by_id(id_prod)
        with col2:
            if st.button("Buscar", use_container_width=True, key="top_search_button"):
                selected_prod = fetch_produto_by_id(id_prod) 
        with col3:
            st.button("Limpar", on_click=clear_input, use_container_width=True, key="clear")

                

    # * Criar Produto
    if st.session_state.options == "cadastrar":
        with st.form("cadastrar_produto", clear_on_submit= True):
            st.subheader("Cadastrar Produto")

            cols = st.columns(2)
            with cols[0]:
                nome = st.text_input("Nome")
                preco = st.number_input("Preço", step=0.01)
            with cols[1]:
                ingredientes = st.text_input("Ingredientes", placeholder="código 1, código 2, ...")
               


    
            col_space, col1, col2 = st.columns([7, 1, 1], gap="small")

            with col1:
                if st.form_submit_button("Cadastrar", use_container_width=True):
                    lista_ingredientes = ingredientes.split(", ")
                    new_prod = create_produto(nome, preco, lista_ingredientes)

                    if new_prod == True:
                        st.toast("Produto cadastrado com sucesso", icon="🎉")
                    else:
                        st.toast(new_prod, icon="⚠️")
            with col2:
                if st.form_submit_button("Cancelar", type="primary", use_container_width=True):
                    pass


    # * Editar produto
    if st.session_state.options == "editar":

        if "changed" not in st.session_state:
            st.session_state.changed = False
        if st.session_state.changed:
            st.session_state.changed = False
            st.toast("Produto editado com sucesso", icon="🎉")


        if selected_prod:
            with st.form("editar_produto", clear_on_submit=True):
                st.subheader("Editar produto")
    
                cols = st.columns(2)
                with cols[0]:
                    codigo = st.number_input("Código", value=selected_prod["id_produto"], disabled=True)
                    nome = st.text_input("Nome", value=selected_prod["nome"])
                    
                with cols[1]:
                    preco = st.number_input("Preço", value=selected_prod["preco"])
                

                col_space, col1, col2 = st.columns([7, 1, 1], gap="small")
                with col1:
                    if st.form_submit_button("Editar", use_container_width=True):
                        edit_ingred = edit_produto(codigo, nome, preco)
                        if edit_ingred == True:
                            st.session_state.changed = True
                            st.rerun()
                        else:
                            st.toast(edit_ingred, icon="⚠️")
                with col2:
                    if st.form_submit_button("Cancelar", type="primary", use_container_width=True):
                        pass

        elif selected_prod == [] and id_prod != "":
            st.toast("Produto não encontrado", icon="⚠️")



    # * Deletar produto
    if st.session_state.options == "deletar":

        if "deleted" not in st.session_state:
            st.session_state.deleted = False
        if st.session_state.deleted:
            st.session_state.deleted = False

            st.toast("Produto deletado com sucesso", icon="🎉")
        

        if selected_prod:
            with st.form("deletar_produto", clear_on_submit=True):
                st.subheader("Deletar produto")

                cols = st.columns(2)
                with cols[0]:
                    codigo = st.number_input("Código", value=selected_prod["id_produto"], disabled=True)
                    nome = st.text_input("Nome", value=selected_prod["nome"], disabled=True)
                with cols[1]:
                    preco = st.number_input("Preço", value=selected_prod["preco"], disabled=True)

                col_space, col1, col2 = st.columns([7, 1, 1], gap="small")

                with col1:
                    if st.form_submit_button("Deletar", use_container_width=True):
                        delete_ingred = delete_produto(id_prod)
                        if delete_ingred:
                            st.session_state.deleted = True
                            st.rerun()
                        else:
                            st.toast("Erro ao deletar produto", icon="⚠️")
                with col2:
                    if st.form_submit_button("Cancelar",type='primary', use_container_width=True):
                        pass
        elif selected_prod == [] and id_prod != "" and st.session_state.deleted == True:
            st.toast("Produto não encontrado", icon="⚠️")                



    st.markdown("<br>", unsafe_allow_html=True)
    st.subheader("Lista de Produtos")


    if "search" not in st.session_state:
        st.session_state.search = "nome"
    st.radio("Buscar por:", ["nome", "código"], key="search", horizontal=True)


    col1, col2, col3 = st.columns([8, 1, 1])
    with col1:
        id_prod = st.text_input("ID do produtos", label_visibility="collapsed", placeholder=f"{st.session_state.search} do produtos", key="search_input")
    
    with col2:
        if st.button("Buscar", use_container_width=True, key="bottom_search_button"):
            pass
    with col3:
        st.button("Limpar", on_click=clear_input, use_container_width=True)
        

    # * Buscar por nome ou exibir todos
    if id_prod:
        if st.session_state.search == "nome":
            data_prod = fetch_produto_by_nome(id_prod)
            df_prod = pd.DataFrame(data_prod)
        if st.session_state.search == "código":
            data_prod = fetch_produto_by_id(id_prod)
            df_prod = pd.DataFrame([data_prod]) 
    else:
        data_prod = fetch_produto()
        df_prod = pd.DataFrame(data_prod)

    if data_prod == []:
        st.error("Nenhum produto encontrado")
    else:
        df_prod.columns = ["Código", "Nome", "Preço(R$)", "Ingredientes"]
        st.dataframe(df_prod, hide_index=True, use_container_width=True)   
        
