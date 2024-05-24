import streamlit as st
import pandas as pd
from utils.page_modules import clear_input
from utils.clien_modules import fetch_cliente, fetch_cliente_by_telefone, fetch_cliente_by_nome, create_cliente, edit_cliente, delete_cliente



# * Página de Clientes
def page_cliente():
    st.title("🧑 Clientes")
    st.markdown("<br>", unsafe_allow_html=True)


    if "options" not in st.session_state:
        st.session_state.options = "cadastrar"
    st.radio("Operações:", ["cadastrar", "editar", "deletar"], key="options", horizontal=True)


    if st.session_state.options != "cadastrar":
        col1, col2, col3 = st.columns([8, 1, 1])
        with col1:
            id_clien = st.text_input("ID do cliente", key="forms_input", placeholder="telefone do cliente", label_visibility="collapsed")
            selected_clien = fetch_cliente_by_telefone(id_clien)
        with col2:
            if st.button("Buscar", use_container_width=True, key="top_search_button"):
                selected_clien = fetch_cliente_by_telefone(id_clien) 
        with col3:
            st.button("Limpar", on_click=clear_input, use_container_width=True, key="clear")

                

    # * Criar cliente
    if st.session_state.options == "cadastrar":
        with st.form("cadastrar_cliente", clear_on_submit= True):
            st.subheader("Cadastrar Cliente")

            cols = st.columns(2)
            with cols[0]:
                nome = st.text_input("Nome")
                telefone_1 = st.text_input("Telefone 1")
                telefone_2 = st.text_input("Telefone 2")
                cep = st.text_input("CEP")
            with cols[1]:
                rua = st.text_input("Rua")
                bairro = st.text_input("Bairro")
                numero = st.text_input("Número")
                complemento = st.text_input("Complemento")
          
    
            col_space, col1, col2 = st.columns([7, 1, 1], gap="small")

            with col1:
                if st.form_submit_button("Cadastrar", use_container_width=True):
                    new_clien = create_cliente(nome, telefone_1, telefone_2, complemento, rua, bairro, numero, cep)

                    if new_clien:
                        st.toast("Cliente cadastrado com sucesso", icon="🎉")
                    else:
                        st.toast("Erro ao cadastrar cliente", icon="⚠️")
            with col2:
                if st.form_submit_button("Cancelar", type="primary", use_container_width=True):
                    pass


    # * Editar cliente
    if st.session_state.options == "editar":

        if "changed" not in st.session_state:
            st.session_state.changed = False
        if st.session_state.changed:
            st.session_state.changed = False
            st.toast("Cliente editado com sucesso", icon="🎉")


        if selected_clien:
            with st.form("editar_cliente", clear_on_submit=True):
                st.subheader("Editar Cliente")
    
                cols = st.columns(2)
                with cols[0]:
                    id = st.text_input("ID", value=selected_clien["id_cliente"], disabled=True)
                    nome = st.text_input("Nome", value=selected_clien["nome"])
                    telefone_1 = st.text_input("Telefone 1", value=selected_clien["telefone_1"])
                    telefone_2 = st.text_input("Telefone 2", value=selected_clien["telefone_2"])
                    cep = st.text_input("CEP", value=selected_clien["cep"])
                with cols[1]:     
                    rua = st.text_input("Rua", value=selected_clien["rua"])
                    bairro = st.text_input("Bairro", value=selected_clien["bairro"])
                    numero = st.text_input("Número", value=selected_clien["numero"])
                    complemento = st.text_input("Complemento", value=selected_clien["complemento"])
                    
                    

                col_space, col1, col2 = st.columns([7, 1, 1], gap="small")
                with col1:
                    if st.form_submit_button("Editar", use_container_width=True):
                        edit_clien = edit_cliente(telefone_1, nome, telefone_1, telefone_2, complemento, rua, bairro, numero, cep)
                        if edit_clien:
                            st.session_state.changed = True
                            st.rerun()
                        else:
                            st.toast("Erro ao editar cliente", icon="⚠️")
                with col2:
                    if st.form_submit_button("Cancelar", type="primary", use_container_width=True):
                        pass

        elif selected_clien == [] and id_clien != "":
            st.toast("cliente não encontrado", icon="⚠️")



    # * Deletar cliente
    if st.session_state.options == "deletar":

        if "deleted" not in st.session_state:
            st.session_state.deleted = False
        if st.session_state.deleted:
            st.session_state.deleted = False

            st.toast("Cliente deletado com sucesso", icon="🎉")
        

        if selected_clien:
            with st.form("deletar_cliente", clear_on_submit=True):
                st.subheader("Deletar Cliente")

                cols = st.columns(2)
                with cols[0]:
                    st.text_input("ID", value=selected_clien["id_cliente"], disabled=True)
                    st.text_input("Nome", value=selected_clien["nome"], disabled=True)
                    st.text_input("Telefone 1", value=selected_clien["telefone_1"], disabled=True)
                    st.text_input("Telefone 2", value=selected_clien["telefone_2"], disabled=True)
                    st.text_input("CEP", value=selected_clien["cep"], disabled=True)
                with cols[1]:
                    st.text_input("Rua", value=selected_clien["rua"], disabled=True)
                    st.text_input("Bairro", value=selected_clien["bairro"], disabled=True)
                    st.text_input("Número", value=selected_clien["numero"], disabled=True)
                    st.text_input("Complemento", value=selected_clien["complemento"], disabled=True)
                    

                col_space, col1, col2 = st.columns([7, 1, 1], gap="small")

                with col1:
                    if st.form_submit_button("Deletar", use_container_width=True):
                        delete_clien = delete_cliente(selected_clien["id_cliente"])
                        if delete_clien:
                            st.session_state.deleted = True
                            st.rerun()
                        else:
                            st.toast("Erro ao deletar cliente", icon="⚠️")
                with col2:
                    if st.form_submit_button("Cancelar",type='primary', use_container_width=True):
                        pass

        elif selected_clien == [] and id_clien != "" and st.session_state.deleted == True:
            st.toast("Cliente não encontrado", icon="⚠️")                



    st.markdown("<br>", unsafe_allow_html=True)
    st.subheader("Lista de Clientes")


    if "search" not in st.session_state:
        st.session_state.search = "nome"
    st.radio("Buscar por:", ["nome", "telefone"], key="search", horizontal=True)


    col1, col2, col3 = st.columns([8, 1, 1])
    with col1:
        id_clien= st.text_input("ID do clientes", label_visibility="collapsed", placeholder=f"{st.session_state.search} do cliente", key="search_input")
    
    with col2:
        if st.button("Buscar", use_container_width=True, key="bottom_search_button"):
            pass
    with col3:
        st.button("Limpar", on_click=clear_input, use_container_width=True)
        

    # * Buscar por nome ou exibir todos
    if id_clien:
        if st.session_state.search == "nome":
            data_clien = fetch_cliente_by_nome(id_clien)
            df_clien = pd.DataFrame(data_clien)
        if st.session_state.search == "telefone":
            data_clien = fetch_cliente_by_telefone(id_clien)
            df_clien = pd.DataFrame([data_clien]) 
    else:
        data_clien = fetch_cliente()
        df_clien = pd.DataFrame(data_clien)

    if data_clien == []:
        st.error("Nenhum cliente encontrado")
    else:
        df_clien.columns = ["ID", "Nome", "Telefone 1", "Telefone 2", "Complemento", "Rua", "Bairro", "Número", "CEP"]
        st.dataframe(df_clien, hide_index=True, use_container_width=True)   
        
