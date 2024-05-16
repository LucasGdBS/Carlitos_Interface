import streamlit as st
import pandas as pd
import numpy as np
import requests
import time


def fetch_funcionario():
    url = "http://localhost:8080/funcionarios/"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        elif response.status_code == 404:
            return []
        
    except Exception:
        return []
        

def fetch_funcionario_by_nome(nome):
    url = f"http://localhost:8080/funcionarios/buscar-por-nome?nome={nome}" 
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        elif response.status_code == 404:
            return []

    except Exception:
        return []

def fetch_funcionario_by_cpf(cpf):
    url = f"http://localhost:8080/funcionarios/buscar-por-cpf?cpf={cpf}"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        elif response.status_code == 404:
            return []
    except Exception:
        return []


def create_funcionario(cpf, nome, salario):
    url = "http://localhost:8080/funcionarios/"
    data = {
        "cpf": cpf,
        "nome": nome,
        "salario": salario
    }
    try:
        response = requests.post(url, json=data)
        if response.status_code == 201:
            return True
        else:
            return False
    except Exception:
        return False


def edit_funcionario_by_cpf(cpf, nome, salario):
    url = f"http://localhost:8080/funcionarios/editar-por-cpf/{cpf}"
    data = {
        "nome": nome,
        "salario": salario
    }
    try:
        response = requests.put(url, json=data)
        if response.status_code == 200:
            return True
        else:
            return False
    except Exception:
        return False

def delete_funcionario(cpf):
    url = f"http://localhost:8080/funcionarios/{cpf}"
    try:
        response = requests.delete(url)
        if response.status_code == 200:
            return True
        else:
            return False
    except Exception:
        return False



def page_funcionario():
    st.title("👨‍💼 Funcionários")
    st.markdown("<br>", unsafe_allow_html=True)


    if "options" not in st.session_state:
        st.session_state.options = "cadastrar"
    st.radio("Operações:", ["cadastrar", "editar", "deletar"], key="options", horizontal=True)



    # * Criar Funcionario
    if st.session_state.options == "cadastrar":
        with st.form("cadastrar_funcionario", clear_on_submit=True):
            st.subheader("Cadastrar Funcionário")

            cols = st.columns(3)
            with cols[0]:
                cpf = st.text_input("CPF")
            with cols[1]:
                nome = st.text_input("Nome")
            with cols[2]:
                salario = st.text_input("Salario")
            
    
            col_space, col1, col2 = st.columns([7, 1, 1], gap="small")
            with col1:
                if st.form_submit_button("Cancelar", type="primary", use_container_width=True):
                    pass
            with col2:
                if st.form_submit_button("Cadastrar", use_container_width=True):
                    new_func = create_funcionario(cpf, nome, salario)
                    if new_func:
                        st.toast("Funcionário cadastrado com sucesso", icon="🎉")
                    else:
                        st.toast("Erro ao cadastrar funcionário", icon="⚠️")



    # * Editar Funcionario
    if st.session_state.options == "editar":

        cpf_func = st.text_input("CPF do funcionário")
        selected_func = fetch_funcionario_by_cpf(cpf_func)
        

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
                    if st.form_submit_button("Cancelar", type="primary", use_container_width=True):
                        pass
                with col2:
                    if st.form_submit_button("Editar", use_container_width=True):
                        edit_func = edit_funcionario_by_cpf(cpf, nome, salario)
                        if edit_func:
                            st.session_state.changed = True
                            st.rerun()
                        else:
                            st.toast("Erro ao editar funcionário", icon="⚠️")

        elif selected_func == [] and cpf_func != "":
            st.toast("Funcionário não encontrado", icon="⚠️")



    # * Deletar Funcionario
    if st.session_state.options == "deletar":
        with st.form("deletar_funcionario", clear_on_submit=True):
            st.subheader("Deletar Funcionário")

            cpf = st.text_input("CPF")


            col_space, col1, col2 = st.columns([7, 1, 1], gap="small")
            with col1:
                if st.form_submit_button("Cancelar", type="primary", use_container_width=True):
                    pass
            with col2:
                if st.form_submit_button("Deletar", use_container_width=True):
                    delete_func = delete_funcionario(cpf)
                    if delete_func:
                        st.toast("Funcionário deletado com sucesso", icon="🎉")
                    else:
                        st.toast("Erro ao deletar funcionário", icon="⚠️")
                    



    st.markdown("<br>", unsafe_allow_html=True)
    st.subheader("Lista de Funcionários")


    if "search" not in st.session_state:
        st.session_state.search = "nome"
    st.radio("Buscar por:", ["nome", "cpf"], key="search", horizontal=True)


    id_func = st.text_input(" ", label_visibility="collapsed", placeholder=f"{st.session_state.search} do funcionário")


    # * Exibir por nome ou exibir todos
    if id_func:
        if st.session_state.search == "nome":
            data_func = fetch_funcionario_by_nome(id_func)
        elif st.session_state.search == "cpf":
            data_func = fetch_funcionario_by_cpf(id_func)
    else:
        data_func = fetch_funcionario()
    

    if data_func == []:
        st.toast("Nenhum funcionário encontrado", icon="⚠️")
    else:
        df_func = pd.DataFrame(data_func)
        df_func.columns = ["CPF", "Nome", "Salário"]
        st.dataframe(df_func, hide_index=True, use_container_width=True)   

