
import requests
import pandas as pd
from utils.clien_modules import fetch_cliente_by_telefone
from utils.prod_modules import fetch_produto_by_nome

def fetch_pedido():
    url = "http://localhost:8080/pedidos/"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        elif response.status_code == 404:
            return []
        
    except Exception:
        return []


def fetch_pedido_by_id(id_pedido):
    url = f"http://localhost:8080/pedidos/buscar-por-id?id={id_pedido}"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        elif response.status_code == 404:
            return []
    except Exception:
        return []


def fetch_pedido_by_name(nome):
    url = f"http://localhost:8080/pedidos/buscar-por-nome?nome={nome}"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        elif response.status_code == 404:
            return []
    except Exception:
        return []


def fetch_pedido_resumo(id_pedido):
    url = f"http://localhost:8080/pedidos/resumo/{id_pedido}"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        elif response.status_code == 404:
            return []
    except Exception:
        return []


def fetch_pedido_resumo_by_atendente(nome_atendente):
    url = f"http://localhost:8080/pedidos/resumo?nome={nome_atendente}"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        elif response.status_code == 404:
            return []
    except Exception:
        return []


def create_pedido(cod_nota, num_pedido, tel_cliente, nome_produtos, cpf_atendente, dt_pedido, forma_pagamento, taxa_entrega, desconto, qntd_input):

    id_cliente = int(fetch_cliente_by_telefone(tel_cliente)["id_cliente"])
    id_produtos= []
    for i in nome_produtos:
        produto = fetch_produto_by_nome(i)[0]["id_produto"]
        id_produtos.append(produto)

    qntd_produtos = [int(n.strip()) for n in qntd_input.split(",")]

    check = 0

    url = "http://localhost:8080/pedidos/"

    for i in range(len(id_produtos)):
        data = {
            "codigoNotalFiscal": cod_nota,
            "numeroPedido": num_pedido,
            "idCliente": id_cliente,
            "produtoId": id_produtos[i],
            "atendenteCpf": cpf_atendente,
            "dtPedido": dt_pedido,
            "formaPagamento": forma_pagamento,
            "taxaEntrega": taxa_entrega,
            "desconto": desconto,
            "qntProduto": qntd_produtos[i]
        }

        response = requests.post(url, json=data)
        if response.status_code == 201:
            check += 1
        else:
            return f"{id_produtos[i]}: {response.text}"

    if check == len(id_produtos):
        return True



def delete_pedido(id_pedido):
    url = f"http://localhost:8080/pedidos/{id_pedido}"
    try:
        response = requests.delete(url)
        if response.status_code == 200:
            return True
        else:
            return False
    except Exception:
        return False