import streamlit as st
import pandas as pd
from utils.page_modules import clear_input
from utils.func_modules import fetch_funcionario, fetch_funcionario_by_cpf, fetch_funcionario_by_nome, create_funcionario, edit_funcionario_by_cpf, delete_funcionario
from utils.aten_modules import create_atendente
from utils.moto_modules import create_motoqueiro
from utils.geren_modules import create_gerente


# * Página de Funcionários
def page_funcionario():
    st.title("👨‍💼 Funcionários")
    st.markdown("<br>", unsafe_allow_html=True)


    if "options" not in st.session_state:
        st.session_state.options = "cadastrar"
    st.radio("Operações:", ["cadastrar", "editar", "deletar"], key="options", horizontal=True)


    if st.session_state.options != "cadastrar":
        col1, col2, col3 = st.columns([8, 1, 1])
        with col1:
            cpf_func = st.text_input("CPF do funcionário", key="forms_input", placeholder="cpf do funcionário", label_visibility="collapsed")
            selected_func = fetch_funcionario_by_cpf(cpf_func)
        with col2:
            if st.button("Buscar", use_container_width=True, key="top_search_button"):
                selected_func = fetch_funcionario_by_cpf(cpf_func)     
        with col3:
            st.button("Limpar", on_click=clear_input, use_container_width=True, key="clear")

                

    # * Criar Funcionario
    if st.session_state.options == "cadastrar":
        with st.form("cadastrar_funcionario", clear_on_submit= True):
            st.subheader("Cadastrar Funcionário")

            cols = st.columns(4)
            with cols[0]:
                cpf = st.text_input("CPF")
            with cols[1]:
                nome = st.text_input("Nome")
            with cols[2]:
                salario = st.text_input("Salario")
            with cols[3]:
                cargo = st.selectbox("Cargo", ["Funcionário", "Atendente", "Motoqueiro", "Gerente"], index=0)
            
            col_space, col1, col2 = st.columns([7, 1, 1], gap="small")

            # ! TERMINAR A TRIBUIÇÃO DOS CARGOS
            with col1:
                if st.form_submit_button("Cadastrar", use_container_width=True):
                    new_func = create_funcionario(cpf, nome, salario)
                    if cargo == "Atendente":
                        new_func = create_atendente(cpf, cpf)
                    if cargo == "Motoqueiro":
                        new_func = create_motoqueiro(cpf, cpf)
                    if new_func:
                        st.toast("Funcionário cadastrado com sucesso", icon="🎉")
                    else:
                        st.toast("Erro ao cadastrar funcionário", icon="⚠️")
            with col2:
                if st.form_submit_button("Cancelar", type="primary", use_container_width=True):
                    pass

    # * Editar Funcionario
    if st.session_state.options == "editar":

        if "changed" not in st.session_state:
            st.session_state.changed = False
        if st.session_state.changed:
            st.session_state.changed = False
            st.toast("Funcionário editado com sucesso", icon="🎉")


        if selected_func:
            with st.form("editar_funcionario", clear_on_submit=True):
                st.subheader("Editar Funcionário")
    
                cols = st.columns(3)
                with cols[0]:
                    cpf = st.text_input("CPF",value=cpf_func, disabled=True)
                with cols[1]:
                    nome = st.text_input("Nome", value=selected_func["nome"])
                with cols[2]:
                    salario = st.text_input("Salario", value=selected_func["salario"])
                

                col_space, col1, col2 = st.columns([7, 1, 1], gap="small")
                with col1:
                    if st.form_submit_button("Editar", use_container_width=True):
                        edit_func = edit_funcionario_by_cpf(cpf, nome, salario)
                        if edit_func:
                            st.session_state.changed = True
                            st.rerun()
                        else:
                            st.toast("Erro ao editar funcionário", icon="⚠️")
                with col2:
                    if st.form_submit_button("Cancelar", type="primary", use_container_width=True):
                        pass

        elif selected_func == [] and cpf_func != "":
            st.toast("Funcionário não encontrado", icon="⚠️")



    # * Deletar Funcionario
    if st.session_state.options == "deletar":

        if "deleted" not in st.session_state:
            st.session_state.deleted = False
        if st.session_state.deleted:
            st.session_state.deleted = False

            st.toast("Funcionário deletado com sucesso", icon="🎉")
        

        if selected_func:
            with st.form("deletar_funcionario", clear_on_submit=True):
                st.subheader("Deletar Funcionário")

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
                        delete_func = delete_funcionario(cpf)
                        if delete_func:
                            st.session_state.deleted = True
                            st.rerun()
                        else:
                            st.toast("Erro ao deletar funcionário", icon="⚠️")
                with col2:
                    if st.form_submit_button("Cancelar",type='primary', use_container_width=True):
                        pass
        elif selected_func == [] and cpf_func != "" and st.session_state.deleted == True:
            st.toast("Funcionário não encontrado", icon="⚠️")                



    st.markdown("<br>", unsafe_allow_html=True)
    st.subheader("Lista de Funcionários")


    if "search" not in st.session_state:
        st.session_state.search = "nome"
    st.radio("Buscar por:", ["nome", "cpf"], key="search", horizontal=True)


    col1, col2, col3 = st.columns([8, 1, 1])
    with col1:
        id_func = st.text_input("ID do funcionário", label_visibility="collapsed", placeholder=f"{st.session_state.search} do funcionário", key="search_input")
    
    with col2:
        if st.button("Buscar", use_container_width=True, key="bottom_search_button"):
            pass
    with col3:
        st.button("Limpar", on_click=clear_input, use_container_width=True)
        

    # * Buscar por nome ou exibir todos
    if id_func:
        if st.session_state.search == "nome":
            data_func = fetch_funcionario_by_nome(id_func)
            df_func = pd.DataFrame(data_func)
        if st.session_state.search == "cpf":
            data_func = fetch_funcionario_by_cpf(id_func)
            df_func = pd.DataFrame([data_func]) 
    else:
        data_func = fetch_funcionario()
        df_func = pd.DataFrame(data_func)

    if data_func == []:
        st.error("Nenhum funcionário encontrado")
    else:
        df_func.columns = ["CPF", "Nome", "Salário"]
        st.dataframe(df_func, hide_index=True, use_container_width=True)   
        
