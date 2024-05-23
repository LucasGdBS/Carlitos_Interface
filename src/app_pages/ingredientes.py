import streamlit as st
import pandas as pd
from utils.page_modules import clear_input
from utils.ingred_modules import fetch_ingrediente, fetch_ingrediente_by_id, fetch_ingrediente_by_nome, create_ingrediente, edit_ingrediente_by_id, delete_ingrediente



# * Página de Ingredientes
def page_ingrediente():
    st.title("🥦 Ingredientes")
    st.markdown("<br>", unsafe_allow_html=True)


    if "options" not in st.session_state:
        st.session_state.options = "cadastrar"
    st.radio("Operações:", ["cadastrar", "editar", "deletar"], key="options", horizontal=True)


    if st.session_state.options != "cadastrar":
        col1, col2, col3 = st.columns([8, 1, 1])
        with col1:
            id_ingred = st.text_input("ID do alimento", key="forms_input", placeholder="código do alimento", label_visibility="collapsed")
            selected_ingred = fetch_ingrediente_by_id(id_ingred)
        with col2:
            if st.button("Buscar", use_container_width=True, key="top_search_button"):
                selected_ingred = fetch_ingrediente_by_id(id_ingred) 
        with col3:
            st.button("Limpar", on_click=clear_input, use_container_width=True, key="clear")

                

    # * Criar Ingrediente
    if st.session_state.options == "cadastrar":
        with st.form("cadastrar_ingrediente", clear_on_submit= True):
            st.subheader("Cadastrar Ingrediente")

            cols = st.columns(2)
            with cols[0]:
                codigo = st.number_input("Código", step=1)
                nome = st.text_input("Nome")
            dt_validade = st.text_input("Data de Validade", placeholder="aaaa-mm-dd")
            with cols[1]:
                quantidade = st.number_input("Quantidade", step=1)
                tipo = st.radio("Tipo", ['Porcionado', 'Fatiado', 'Unitario'], horizontal=True)
          
    
            col_space, col1, col2 = st.columns([7, 1, 1], gap="small")

            with col1:
                if st.form_submit_button("Cadastrar", use_container_width=True):
                    new_ingred = create_ingrediente(nome, dt_validade, quantidade, codigo, tipo)

                    if new_ingred:
                        st.toast("Ingrediente cadastrado com sucesso", icon="🎉")
                    else:
                        st.toast("Erro ao cadastrar ingrediente", icon="⚠️")
            with col2:
                if st.form_submit_button("Cancelar", type="primary", use_container_width=True):
                    pass


    # * Editar Ingrediente
    if st.session_state.options == "editar":

        if "changed" not in st.session_state:
            st.session_state.changed = False
        if st.session_state.changed:
            st.session_state.changed = False
            st.toast("Ingrediente editado com sucesso", icon="🎉")


        if selected_ingred:
            with st.form("editar_ingrediente", clear_on_submit=True):
                st.subheader("Editar Ingrediente")
    
                cols = st.columns(2)
                with cols[0]:
                    codigo = st.number_input("Código", value=selected_ingred["codigo"], disabled=True)
                    nome = st.text_input("Nome", value=selected_ingred["nome"])
                    dt_validade = st.text_input("Data de Validade", value=selected_ingred["dtValidade"])
                with cols[1]:
                    quantidade = st.number_input("Quantidade", value=selected_ingred["quantidade"])
                    tipo = st.text_input("Tipo", value=selected_ingred["tipoAlimento"])
                

                col_space, col1, col2 = st.columns([7, 1, 1], gap="small")
                with col1:
                    if st.form_submit_button("Editar", use_container_width=True):
                        edit_ingred = edit_ingrediente_by_id(id_ingred, nome, dt_validade, quantidade, codigo, tipo)
                        if edit_ingred:
                            st.session_state.changed = True
                            st.rerun()
                        else:
                            st.toast("Erro ao editar ingrediente", icon="⚠️")
                with col2:
                    if st.form_submit_button("Cancelar", type="primary", use_container_width=True):
                        pass

        elif selected_ingred == [] and id_ingred != "":
            st.toast("Ingrediente não encontrado", icon="⚠️")



    # * Deletar Ingrediente
    if st.session_state.options == "deletar":

        if "deleted" not in st.session_state:
            st.session_state.deleted = False
        if st.session_state.deleted:
            st.session_state.deleted = False

            st.toast("Ingrediente deletado com sucesso", icon="🎉")
        

        if selected_ingred:
            with st.form("deletar_ingrediente", clear_on_submit=True):
                st.subheader("Deletar Ingrediente")

                cols = st.columns(2)
                with cols[0]:
                    codigo = st.number_input("Código", value=selected_ingred["codigo"], disabled=True)
                    nome = st.text_input("Nome", value=selected_ingred["nome"], disabled=True)
                    dt_validade = st.text_input("Data de Validade", value=selected_ingred["dtValidade"], disabled=True)
                with cols[1]:
                    quantidade = st.number_input("Quantidade", value=selected_ingred["quantidade"], disabled=True)
                    tipo = st.text_input("Tipo", value=selected_ingred["tipoAlimento"], disabled=True)

                col_space, col1, col2 = st.columns([7, 1, 1], gap="small")

                with col1:
                    if st.form_submit_button("Deletar", use_container_width=True):
                        delete_ingred = delete_ingrediente(id_ingred)
                        if delete_ingred:
                            st.session_state.deleted = True
                            st.rerun()
                        else:
                            st.toast("Erro ao deletar ingrediente", icon="⚠️")
                with col2:
                    if st.form_submit_button("Cancelar",type='primary', use_container_width=True):
                        pass
        elif selected_ingred == [] and id_ingred != "" and st.session_state.deleted == True:
            st.toast("Ingrediente não encontrado", icon="⚠️")                



    st.markdown("<br>", unsafe_allow_html=True)
    st.subheader("Lista de Ingredientes")


    if "search" not in st.session_state:
        st.session_state.search = "nome"
    st.radio("Buscar por:", ["nome", "código"], key="search", horizontal=True)


    col1, col2, col3 = st.columns([8, 1, 1])
    with col1:
        id_ingred = st.text_input("ID do Ingredientes", label_visibility="collapsed", placeholder=f"{st.session_state.search} do Ingredientes", key="search_input")
    
    with col2:
        if st.button("Buscar", use_container_width=True, key="bottom_search_button"):
            pass
    with col3:
        st.button("Limpar", on_click=clear_input, use_container_width=True)
        

    # * Buscar por nome ou exibir todos
    if id_ingred:
        if st.session_state.search == "nome":
            data_ingred = fetch_ingrediente_by_nome(id_ingred)
            df_ingred = pd.DataFrame(data_ingred)
        if st.session_state.search == "código":
            data_ingred = fetch_ingrediente_by_id(id_ingred)
            df_ingred = pd.DataFrame([data_ingred]) 
    else:
        data_ingred = fetch_ingrediente()
        df_ingred = pd.DataFrame(data_ingred)

    if data_ingred == []:
        st.error("Nenhum ingrediente encontrado")
    else:
        #df_ingred.columns = ["CPF", "Nome", "Salário"]
        st.dataframe(df_ingred, hide_index=True, use_container_width=True)   
        
