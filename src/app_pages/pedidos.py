import streamlit as st
import pandas as pd


def page_pedido():
    st.title("🧾 Pedidos")
    st.markdown("<br>", unsafe_allow_html=True)
    

    with st.form("cadastro_pedidos", clear_on_submit=True):
        st.subheader("Cadastro de Pedidos")

        cols = st.columns(2)

        with cols[0]:
            num_pedido = st.text_input("Numero do Pedido")
            valor_total = st.number_input("Valor Total", value=None)
            dt_pedido = st.date_input("Data do Pedido", value=None)
            forma_pagamento = st.text_input("Forma de Pagamento")
            taxa_entrega = st.number_input("Taxa de Entrega", value=None)

        with cols[1]:
            desconto = st.number_input("Desconto", value=None)
            qnt_produto = st.number_input("Quantidade de Produtos", value=None)
            telefone_cliente = st.text_input("Telefone do Cliente")
            id_produto = st.text_input("ID do Produto")
            cpf_funcionario = st.text_input("CPF do Funcionario")

        
        st.markdown("<br>", unsafe_allow_html=True)

        if st.form_submit_button("Cadastrar"):
            st.write("Pedido cadastrado com sucesso")
        


    st.markdown("<br>", unsafe_allow_html=True)
    st.subheader("Lista de Pedidos")


    sample_data = [
        {
            "num_pedido": "123",
            "valor_total": 100.00,
            "dt_pedido": "01/01/2022",
            "forma_pagamento": "Dinheiro",
            "taxa_entrega": 5.00,
            "desconto": 0.00,
            "qnt_produto": 2,
            "telefone_cliente": "(11) 99999-9999",
            "id_produto": "123",
            "cpf_funcionario": "123.456.789-00"
        },
        {
            "num_pedido": "456",
            "valor_total": 150.00,
            "dt_pedido": "01/01/2022",
            "forma_pagamento": "Cartão",
            "taxa_entrega": 5.00,
            "desconto": 0.00,
            "qnt_produto": 3,
            "telefone_cliente": "(11) 99999-9999",
            "id_produto": "123",
            "cpf_funcionario": "123.456.789-00"
        },
        {
            "num_pedido": "789",
            "valor_total": 200.00,
            "dt_pedido": "01/01/2022",
            "forma_pagamento": "Pix",
            "taxa_entrega": 5.00,
            "desconto": 0.00,
            "qnt_produto": 4,
            "telefone_cliente": "(11) 99999-9999",
            "id_produto": "123",
            "cpf_funcionario": "123.456.789-00"
        },
        {
            "num_pedido": "101",
            "valor_total": 250.00,
            "dt_pedido": "01/01/2022",
            "forma_pagamento": "Dinheiro",
            "taxa_entrega": 5.00,
            "desconto": 0.00,
            "qnt_produto": 5,
            "telefone_cliente": "(11) 99999-9999",
            "id_produto": "123",
            "cpf_funcionario": "123.456.789-00"
        
        }
    ]


    df_pedido = pd.DataFrame(sample_data)
    df_pedido.columns = ["Numero do Pedido", "Valor Total", "Data do Pedido", "Forma de Pagamento", "Taxa de Entrega", "Desconto", "Quantidade de Produtos", 
                            "Telefone do Cliente", "ID do Produto", "CPF do Funcionario"]

    st.dataframe(df_pedido, hide_index=True, use_container_width=True)   
    