
import requests

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


def create_pedido(cod_nota, num_pedido, id_cliente, id_produto, cpf_atendente, dt_pedido, forma_pagamento, taxa_entrega, desconto, qnt_produto):
    url = "http://localhost:8080/pedidos/"
    data = {
        "codigoNotalFiscal": cod_nota,
        "numeroPedido": num_pedido,
        "idCliente": id_cliente,
        "produtoId": id_produto,
        "atendenteCpf": cpf_atendente,
        "dtPedido": dt_pedido,
        "formaPagamento": forma_pagamento,
        "taxaEntrega": taxa_entrega,
        "desconto": desconto,
        "qntProduto": qnt_produto
    }
    try:
        response = requests.post(url, json=data)
        if response.status_code == 201:
            return True
        else:
            return False
    except Exception:
        return False


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