import streamlit as st
import pandas as pd
from utils.page_modules import clear_input
from utils.aten_modules import fetch_atendente, fetch_atendente_by_cpf, fetch_atendente_by_nome, fetch_atendente_by_geren_cpf, create_atendente, edit_atendente_by_cpf, delete_atendente
from utils.func_modules import fetch_funcionario, fetch_funcionario_by_cpf



# * Página dos atendentes
def page_atendente():
    st.title("☎️ Atendentes")
    st.markdown("<br>", unsafe_allow_html=True)


    if "options" not in st.session_state:
        st.session_state.options = "atribuir cargo"
    st.radio("Operações:", ["atribuir cargo", "editar", "deletar"], key="options", horizontal=True)


    if st.session_state.options == "atribuir cargo":
        values = fetch_funcionario()
        values = [i["cpf"] for i in values]
        cpf_aten = st.selectbox("CPF do funcionário", values, placeholder="cpf do funcionário", label_visibility="collapsed", index=0)
        selected_aten = fetch_funcionario_by_cpf(cpf_aten)
    else:
        values = fetch_atendente()
        values = [i["cpf"] for i in values]
        cpf_aten = st.selectbox("CPF do atendente", values, placeholder="cpf do atendente", label_visibility="collapsed", index=0)
        selected_aten = fetch_atendente_by_cpf(cpf_aten)
                

    # * Criar Atendente
    if st.session_state.options == "atribuir cargo":

        if "changed" not in st.session_state:
            st.session_state.changed = False
        if st.session_state.changed:
            st.session_state.changed = False
            st.toast("Cargo de atendente atribuído com sucesso", icon="🎉")

        if selected_aten:
            with st.form("atribuir_cargo", clear_on_submit= True):
                st.subheader("Atribuir Cargo de Atendente")

                cols = st.columns(4)
                with cols[0]:
                    cpf = st.text_input("CPF",value=cpf_aten, disabled=True)
                with cols[1]:
                    nome = st.text_input("Nome", value=selected_aten["nome"], disabled=True)
                with cols[2]:
                    cpf_gerente = st.text_input("CPF do Gerente")
                with cols[3]:
                    turno =  st.radio("Turno:", ["MANHÃ", "NOITE"], horizontal=True)
                
                
                col_space, col1, col2 = st.columns([7, 1, 1], gap="small")

                with col1:
                    if st.form_submit_button("Atribuir", use_container_width=True):
                        new_aten = create_atendente(cpf, turno, cpf_gerente)
                        if new_aten:
                            st.session_state.changed = True
                            st.rerun()
                        else:
                            st.toast("Erro ao atribuir cargo", icon="⚠️")
                with col2:
                    if st.form_submit_button("Cancelar", type="primary", use_container_width=True):
                        pass


    # * Editar atendente
    if st.session_state.options == "editar":

        if "changed" not in st.session_state:
            st.session_state.changed = False
        if st.session_state.changed:
            st.session_state.changed = False
            st.toast("Atendente editado com sucesso", icon="🎉")


        if selected_aten:
            with st.form("editar_atendente", clear_on_submit=True):
                st.subheader("Editar Atendente")
    
                cols = st.columns(4)
                with cols[0]:
                    cpf = st.text_input("CPF",value=cpf_aten, disabled=True)
                with cols[1]:
                    nome = st.text_input("Nome", value=selected_aten["nome"], disabled=True)
                with cols[2]:
                    cpf_gerente = st.text_input("CPF do Gerente", value=selected_aten["cpf_gerente"], disabled=True)
                with cols[3]:
                    if selected_aten["turno"] == "MANHÃ":
                        turno = st.radio("Turno:", ["MANHÃ", "NOITE"], index=0, horizontal=True)
                    elif selected_aten["turno"] == "NOITE":
                        turno = st.radio("Turno:", ["MANHÃ", "NOITE"], index=1, horizontal=True)
                    
                

                col_space, col1, col2 = st.columns([7, 1, 1], gap="small")
                with col1:
                    if st.form_submit_button("Editar", use_container_width=True):
                        edit_aten = edit_atendente_by_cpf(cpf, turno)
                        if edit_aten:
                            st.session_state.changed = True
                            st.rerun()
                        else:
                            st.toast("Erro ao editar atendente", icon="⚠️")
                with col2:
                    if st.form_submit_button("Cancelar", type="primary", use_container_width=True):
                        pass

        elif selected_aten == [] and cpf_aten != "":
            st.toast("atendente não encontrado", icon="⚠️")



    # * Deletar atendente
    if st.session_state.options == "deletar":

        if "deleted" not in st.session_state:
            st.session_state.deleted = False
        if st.session_state.deleted:
            st.session_state.deleted = False

            st.toast("atendente deletado com sucesso", icon="🎉")
        

        if selected_aten:
            with st.form("deletar_atendente", clear_on_submit=True):
                st.subheader("Deletar Atendente")

                cols = st.columns(4)
                with cols[0]:
                    cpf = st.text_input("CPF", value=cpf_aten, disabled=True)
                with cols[1]:
                    nome = st.text_input("Nome", value=selected_aten["nome"], disabled=True)
                with cols[2]:
                    cpf_gerente = st.text_input("CPF do Gerente", value=selected_aten["cpf_gerente"], disabled=True)
                with cols[3]:
                    if selected_aten["turno"] == "MANHÃ":
                        ind = 0
                    elif selected_aten["turno"] == "NOITE":
                        ind = 1
                    turno = st.radio("Turno:", ["MANHÃ", "NOITE"], index=ind, horizontal=True, disabled=True)


                col_space, col1, col2 = st.columns([7, 1, 1], gap="small")

                with col1:
                    if st.form_submit_button("Deletar", use_container_width=True):
                        delete_func = delete_atendente(cpf)
                        if delete_func:
                            st.session_state.deleted = True
                            st.rerun()
                        else:
                            st.toast("Erro ao deletar atendente", icon="⚠️")
                with col2:
                    if st.form_submit_button("Cancelar",type='primary', use_container_width=True):
                        pass
        elif selected_aten == [] and cpf_aten != "" and st.session_state.deleted == True:
            st.toast("atendente não encontrado", icon="⚠️")                



    st.markdown("<br>", unsafe_allow_html=True)
    st.subheader("Lista dos Atendentes")


    if "search" not in st.session_state:
        st.session_state.search = "nome"
    st.radio("Buscar por:", ["nome", "cpf", "cpf do gerente"], key="search", horizontal=True)


    col1, col2, col3 = st.columns([8, 1, 1])
    with col1:
        id_aten = st.text_input("ID do atendente", label_visibility="collapsed", placeholder=f"{st.session_state.search} do atendente", key="search_input")
    
    with col2:
        if st.button("Buscar", use_container_width=True, key="bottom_search_button"):
            pass
    with col3:
        st.button("Limpar", on_click=clear_input, use_container_width=True)
        

    # * Buscar por nome, por cpf ou exibir todos
    if id_aten:
        if st.session_state.search == "nome":
            data_aten = fetch_atendente_by_nome(id_aten)
            df_aten = pd.DataFrame(data_aten)
        if st.session_state.search == "cpf":
            data_aten = fetch_atendente_by_cpf(id_aten)
            df_aten = pd.DataFrame([data_aten]) 
        if st.session_state.search == "cpf do gerente":
            data_aten = fetch_atendente_by_geren_cpf(id_aten)
            df_aten = pd.DataFrame(data_aten)
    else:
        data_aten = fetch_atendente()
        df_aten = pd.DataFrame(data_aten)

    if data_aten == []:
        st.error("Nenhum atendente encontrado")
    else:
        df_aten.columns = ["CPF", "Nome", "Salário", "Turno", "CPF Gerente", "Nome Gerente"]
        st.dataframe(df_aten, hide_index=True, use_container_width=True)   
        
