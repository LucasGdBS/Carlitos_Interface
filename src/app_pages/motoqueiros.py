import streamlit as st
import pandas as pd
from utils.page_modules import clear_input
from utils.moto_modules import fetch_motoqueiro, fetch_motoqueiro_by_cpf, fetch_motoqueiro_by_nome, create_motoqueiro, edit_motoqueiro_by_cpf, delete_motoqueiro
from utils.func_modules import fetch_funcionario


# * Página dos motoqueiros
def page_motoqueiro():
    st.title("🏍️ Motoqueiros")
    st.markdown("<br>", unsafe_allow_html=True)


    if "options" not in st.session_state:
        st.session_state.options = "atribuir cargo"
    st.radio("Operações:", ["atribuir cargo", "editar", "deletar"], key="options", horizontal=True)


    values = fetch_funcionario()
    values = [i["cpf"] for i in values]



    cpf_moto = st.selectbox("CPF do motoqueiro", values, placeholder="cpf do motoqueiro", label_visibility="collapsed", index=0)
    selected_moto = fetch_motoqueiro_by_cpf(cpf_moto)
    
        
                

    # * Criar Motoqueiro
    if st.session_state.options == "atribuir cargo":

        if "changed" not in st.session_state:
            st.session_state.changed = False
        if st.session_state.changed:
            st.session_state.changed = False
            st.toast("Cargo de motoqueiro atribuído com sucesso", icon="🎉")

        if selected_moto:
            with st.form("atribuir_cargo", clear_on_submit= True):
                st.subheader("Atribuir Cargo de Motoqueiro")

                cols = st.columns(2)
                with cols[0]:
                    cpf = st.text_input("CPF",value=cpf_moto, disabled=True)
                with cols[1]:
                    cpf_gerente = st.text_input("CPF do Gerente")
                
                
                col_space, col1, col2 = st.columns([7, 1, 1], gap="small")

                with col1:
                    if st.form_submit_button("Atribuir", use_container_width=True):
                        new_moto = create_motoqueiro(cpf, cpf_gerente)	
                        if new_moto:
                            st.session_state.changed = True
                            st.rerun()
                        else:
                            st.toast("Erro ao atribuir cargo", icon="⚠️")
                with col2:
                    if st.form_submit_button("Cancelar", type="primary", use_container_width=True):
                        pass


    # * Editar Motoqueiro
    if st.session_state.options == "editar":

        if "changed" not in st.session_state:
            st.session_state.changed = False
        if st.session_state.changed:
            st.session_state.changed = False
            st.toast("Motoqueiro editado com sucesso", icon="🎉")


        if selected_moto:
            with st.form("editar_motoqueiro", clear_on_submit=True):
                st.subheader("Editar Motoqueiro")
    
                cols = st.columns(2)
                with cols[0]:
                    cpf = st.text_input("CPF",value=cpf_moto, disabled=True)
                with cols[1]:
                    cpf_gerente = st.text_input("CPF do Gerente", value=selected_moto["gerenteMotoqueiro_cpf"])
      
                

                col_space, col1, col2 = st.columns([7, 1, 1], gap="small")
                with col1:
                    if st.form_submit_button("Editar", use_container_width=True):
                        edit_moto = edit_motoqueiro_by_cpf(cpf, cpf_gerente)
                        if edit_moto:
                            st.session_state.changed = True
                            st.rerun()
                        else:
                            st.toast("Erro ao editar motoqueiro", icon="⚠️")
                with col2:
                    if st.form_submit_button("Cancelar", type="primary", use_container_width=True):
                        pass

        elif selected_moto == [] and cpf_moto != "":
            st.toast("Motoqueiro não encontrado", icon="⚠️")



    # * Deletar Motoqueiro
    if st.session_state.options == "deletar":

        if "deleted" not in st.session_state:
            st.session_state.deleted = False
        if st.session_state.deleted:
            st.session_state.deleted = False

            st.toast("Motoqueiro deletado com sucesso", icon="🎉")
        

        if selected_moto:
            with st.form("deletar_motoqueiro", clear_on_submit=True):
                st.subheader("Deletar Motoqueiro")

                cols = st.columns(2)
                with cols[0]:
                    cpf = st.text_input("CPF", value=cpf_moto, disabled=True)
                with cols[1]:
                    cpf_gerente = st.text_input("CPF do Gerente", value=selected_moto["gerenteMotoqueiro_cpf"], disabled=True)
                

                col_space, col1, col2 = st.columns([7, 1, 1], gap="small")

                with col1:
                    if st.form_submit_button("Deletar", use_container_width=True):
                        delete_func = delete_motoqueiro(cpf)
                        if delete_func:
                            st.session_state.deleted = True
                            st.rerun()
                        else:
                            st.toast("Erro ao deletar motoqueiro", icon="⚠️")
                with col2:
                    if st.form_submit_button("Cancelar",type='primary', use_container_width=True):
                        pass
        elif selected_moto == [] and cpf_moto != "" and st.session_state.deleted == True:
            st.toast("Motoqueiro não encontrado", icon="⚠️")                



    st.markdown("<br>", unsafe_allow_html=True)
    st.subheader("Lista dos Motoqueiros")


    if "search" not in st.session_state:
        st.session_state.search = "nome"
    st.radio("Buscar por:", ["nome", "cpf"], key="search", horizontal=True)


    col1, col2, col3 = st.columns([8, 1, 1])
    with col1:
        id_moto = st.text_input("ID do motoqueiro", label_visibility="collapsed", placeholder=f"{st.session_state.search} do motoqueiro", key="search_input")
    
    with col2:
        if st.button("Buscar", use_container_width=True, key="bottom_search_button"):
            pass
    with col3:
        st.button("Limpar", on_click=clear_input, use_container_width=True)
        

    # * Buscar por nome, por cpf ou exibir todos
    if id_moto:
        if st.session_state.search == "nome":
            data_moto = fetch_motoqueiro_by_nome(id_moto)
            df_moto = pd.DataFrame(data_moto)
        if st.session_state.search == "cpf":
            data_moto = fetch_motoqueiro_by_cpf(id_moto)
            df_moto = pd.DataFrame([data_moto]) 
    else:
        data_moto = fetch_motoqueiro()
        df_moto = pd.DataFrame(data_moto)

    if data_moto == []:
        st.error("Nenhum Motoqueiro encontrado")
    else:
        df_moto.columns = ["CPF", "Nome", "Salário", "CPF Gerente", "Nome Gerente"]
        st.dataframe(df_moto, hide_index=True, use_container_width=True)   
        
