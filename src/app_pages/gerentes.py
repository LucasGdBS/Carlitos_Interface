from utils.geren_modules import fetch_gerente, fetch_gerente_by_nome, fetch_gerente_by_cpf, create_gerente, delete_gerente
from utils.func_modules import fetch_funcionario, fetch_funcionario_by_cpf
from utils.page_modules import clear_input
import streamlit as st
import pandas as pd


# * Página de Gerentes
def page_gerente():
    st.title("💼 Gerentes")
    st.markdown("<br>", unsafe_allow_html=True)


    if "options" not in st.session_state:
        st.session_state.options = "atribuir cargo"
    st.radio("Operações:", ["atribuir cargo", "deletar"], key="options", horizontal=True)

    
    # cpf_func = st.text_input("CPF do gerente", key="forms_input", placeholder="cpf do gerente", label_visibility="collapsed")
    values = fetch_funcionario()
    values = [i["cpf"] for i in values]
    
    cpf_func = st.selectbox("CPF do gerente", values, key="forms_input", placeholder="cpf do gerente", label_visibility="collapsed", index=0)
    selected_func = fetch_funcionario_by_cpf(cpf_func)


            
    # * Atribuir cargo de gerência
    if st.session_state.options == "atribuir cargo":

        if "changed" not in st.session_state:
            st.session_state.changed = False
        if st.session_state.changed:
            st.session_state.changed = False
            st.toast("Cargo de gerência atribuído com sucesso", icon="🎉")


        if selected_func:
            with st.form("atribuir_cargo", clear_on_submit=True):
                st.subheader("Atribuir Cargo de Gerência")
    
                cols = st.columns(2)
                with cols[0]:
                    cpf = st.text_input("CPF",value=cpf_func, disabled=True)
                with cols[1]:
                    nome = st.text_input("Nome", value=selected_func["nome"], disabled=True)
                

                col_space, col1, col2 = st.columns([7, 1, 1], gap="small")
                with col1:
                    if st.form_submit_button("Atribuir", use_container_width=True):
                        edit_func = create_gerente(cpf)
                        if edit_func:
                            st.session_state.changed = True
                            st.rerun()
                        else:
                            st.toast("Erro ao atribuir cargo", icon="⚠️")
                with col2:
                    if st.form_submit_button("Cancelar", type="primary", use_container_width=True):
                        pass

        elif selected_func == [] and cpf_func != "":
            st.toast("Funcionário não encontrado", icon="⚠️")



    # * Deletar gerente
    if st.session_state.options == "deletar":

        if "deleted" not in st.session_state:
            st.session_state.deleted = False
        if st.session_state.deleted:
            st.session_state.deleted = False

            st.toast("Gerente deletado com sucesso", icon="🎉")
        

        if selected_func:
            with st.form("deletar_gerente", clear_on_submit=True):
                st.subheader("Deletar Gerente")

                cols = st.columns(3)
                with cols[0]:
                    cpf = st.text_input("CPF", value=cpf_func, disabled=True)
                with cols[1]:
                    nome = st.text_input("Nome", value=selected_func["nome"], disabled=True)
                with cols[2]:
                    salario = st.text_input("Salario", value=selected_func["salario"], disabled=True)
                

                col_space, col1, col2 = st.columns([7, 1, 1], gap="small")

                with col1:
                    if st.form_submit_button("Deletar", use_container_width=True):
                        delete_func = delete_gerente(cpf)
                        if delete_func:
                            st.session_state.deleted = True
                            st.rerun()
                        else:
                            st.toast("Erro ao deletar gerente", icon="⚠️")
                with col2:
                    if st.form_submit_button("Cancelar",type='primary', use_container_width=True):
                        pass
        elif selected_func == [] and cpf_func != "" and st.session_state.deleted == True:
            st.toast("Gerente não encontrado", icon="⚠️")                



    st.markdown("<br>", unsafe_allow_html=True)
    st.subheader("Lista de Gerentes")


    if "search" not in st.session_state:
        st.session_state.search = "nome"
    st.radio("Buscar por:", ["nome", "cpf"], key="search", horizontal=True)


    col1, col2, col3 = st.columns([8, 1, 1])
    with col1:
        id_func = st.text_input("ID do gerente", label_visibility="collapsed", placeholder=f"{st.session_state.search} do gerente", key="search_input")
    
    with col2:
        if st.button("Buscar", use_container_width=True, key="bottom_search_button"):
            pass
    with col3:
        st.button("Limpar", on_click=clear_input, use_container_width=True)
        

    # * Buscar por nome ou exibir todos
    if id_func:
        if st.session_state.search == "nome":
            data_func = fetch_gerente_by_nome(id_func)
            df_func = pd.DataFrame(data_func)
        if st.session_state.search == "cpf":
            data_func = fetch_gerente_by_cpf(id_func)
            df_func = pd.DataFrame([data_func]) 
    else:
        data_func = fetch_gerente()
        df_func = pd.DataFrame(data_func)

    if data_func == []:
        st.error("Nenhum funcionário encontrado")
    else:
        df_func.columns = ["CPF", "Nome", "Salário"]
        st.dataframe(df_func, hide_index=True, use_container_width=True)   
        
