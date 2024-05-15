import streamlit as st
import pandas as pd
import numpy as np
import requests



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




def page_funcionario():
    st.title("👨‍💼 Funcionarios")
    st.markdown("<br>", unsafe_allow_html=True)



    # * Criar Funcionario
    with st.form("cadastrar_funcionario", clear_on_submit=True):
        st.subheader("Cadastrar Funcionário")
        
        cols = st.columns(3)
        with cols[0]:
            cpf = st.text_input("CPF")
        with cols[1]:
            nome = st.text_input("Nome")
        with cols[2]:
            salario = st.text_input("Salario")
        
        st.markdown("<br>", unsafe_allow_html=True)

        if st.form_submit_button("Cadastrar"):
            new_func = create_funcionario(cpf, nome, salario)
            if new_func:
                st.toast("Funcionário cadastrado com sucesso", icon="🎉")
            else:
                st.toast("Erro ao cadastrar funcionário", icon="⚠️")



    # * Editar Funcionario
    with st.form("editar_funcionario", clear_on_submit=True):
        st.subheader("Editar Funcionário")

        cols = st.columns(3)
        with cols[0]:
            cpf = st.text_input("CPF")
        with cols[1]:
            nome = st.text_input("Nome")
        with cols[2]:
            salario = st.text_input("Salario")
        
        st.markdown("<br>", unsafe_allow_html=True)

        if st.form_submit_button("Editar"):
            edit_func = edit_funcionario_by_cpf(cpf, nome, salario)
            if edit_func:
                st.toast("Funcionário editado com sucesso", icon="🎉")
            else:
                st.toast("Erro ao editar funcionário", icon="⚠️")



    st.markdown("<br>", unsafe_allow_html=True)
    st.subheader("Lista de Funcionários")



    # * Exibir por nome ou exibir todos
    name_func = st.text_input("Buscar por nome")
    if name_func:
        data_func = fetch_funcionario_by_nome(name_func)
    else:
        data_func = fetch_funcionario()


    if data_func == []:
        st.toast("Nenhum funcionário encontrado", icon="⚠️")
    else:
        df_func = pd.DataFrame(data_func)
        df_func.columns = ["CPF", "Nome", "Salário"]
        st.dataframe(df_func, hide_index=True, use_container_width=True)   
    